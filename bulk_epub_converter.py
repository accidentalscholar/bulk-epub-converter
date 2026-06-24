# ==========================================
# Bulk EPUB Converter 
# Version: 1.4
# Citation: Pundir, V. (2026, June 24). Word Metadata Extractor Version (1.4). Retrieved from https://github.com/accidentalscholar/bulk-epub-converter. 
# Citation: RIS and BibTeX files included for referencing software.
# Tested in: Python 3.10.9 64 bit packaged by Anaconda, Inc.
# Reporsitory: https://github.com/accidentalscholar/bulk-epub-converter
# Provided under: GNU AFFERO GENERAL PUBLIC LICENSE (see accompanying license file)
# ==========================================

import sys
import subprocess
import importlib
import os
import glob
import tkinter as tk
from tkinter import filedialog
import warnings
import re

def load_custom_paths(file_name="path.txt"):
    """
    Reads a text file for custom directory paths and appends them to 
    sys.path (for Python modules) and os.environ["PATH"] (for compiled binaries).
    """
    script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
    path_file = os.path.join(script_dir, file_name)
    
    if os.path.exists(path_file):
        print(f"[Info] Found custom path configuration: {path_file}")
        with open(path_file, 'r', encoding='utf-8') as f:
            for line in f:
                clean_path = line.strip()
                if clean_path and not clean_path.startswith('#'):
                    if os.path.isdir(clean_path):
                        if clean_path not in sys.path:
                            sys.path.append(clean_path)
                        if clean_path not in os.environ.get("PATH", ""):
                            os.environ["PATH"] = clean_path + os.pathsep + os.environ.get("PATH", "")
                        print(f"       -> Added path: {clean_path}")
    else:
        pass

warnings.filterwarnings('ignore')
load_custom_paths()

def install_and_import(package, import_name=None):
    import_name = import_name or package
    try:
        importlib.import_module(import_name)
    except ImportError:
        print(f"[Info] Library '{import_name}' not found. Attempting to install '{package}' via pip...")
        try:
            result = subprocess.run([sys.executable, "-m", "pip", "install", package], capture_output=True, text=True)
            if result.returncode == 0:
                importlib.invalidate_caches()
                importlib.import_module(import_name)
                print(f"[Success] Successfully installed {package}.")
            else:
                print(f"\n[ERROR] Pip installation failed for '{package}'.")
                print("Please install it manually by running the following command in your OS console:")
                print(f"    pip install {package}")
                print(f"\n--- Pip Error Output ---\n{result.stderr.strip()}\n------------------------\n")
                raise RuntimeError(f"Manual installation required for {package}")
        except Exception as e:
            if isinstance(e, RuntimeError):
                raise e
            raise RuntimeError(f"Manual installation required for {package}")

print("Checking and loading required libraries. This may take a moment...")
install_and_import("PyMuPDF", "fitz")
install_and_import("python-docx", "docx")

import fitz
import docx

def get_target_folder():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder_path = filedialog.askdirectory(title="Select Folder Containing EPUB Files (or Cancel to Exit)")
    root.destroy()
    return folder_path

def scrub_xml_characters(text):
    return re.sub(r'[^\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]', '', text)

def convert_epub(epub_path, pdf_dir, docx_dir, txt_dir):
    base_name = os.path.splitext(os.path.basename(epub_path))[0]
    print(f"\nProcessing: {base_name}.epub")
    try:
        doc = fitz.open(epub_path)
        print(f"  -> Generating PDF...")
        pdf_path = os.path.join(pdf_dir, f"{base_name}.pdf")
        pdf_bytes = doc.convert_to_pdf()
        with open(pdf_path, "wb") as f:
            f.write(pdf_bytes)
        print(f"  -> Created PDF:  {pdf_path}")
        text_parts = [page.get_text() for page in doc]
        full_text = "\n".join(text_parts)
        txt_path = os.path.join(txt_dir, f"{base_name}.txt")
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"  -> Created TXT:  {txt_path}")
        docx_path = os.path.join(docx_dir, f"{base_name}.docx")
        word_doc = docx.Document()
        for para in full_text.split('\n'):
            clean_para = para.strip()
            if clean_para:
                word_doc.add_paragraph(scrub_xml_characters(clean_para))
        word_doc.save(docx_path)
        print(f"  -> Created DOCX: {docx_path}")
        doc.close()
    except Exception as e:
        print(f"  -> [Error] Failed to process {base_name}.epub: {e}")

def main():
    print(f"Starting EPUB Converter v{__version__}...")
    while True:
        folder_path = get_target_folder()
        if not folder_path:
            print("No folder selected or user cancelled. Exiting.")
            break
        epub_files = glob.glob(os.path.join(folder_path, "*.epub"))
        if not epub_files:
            print(f"No .epub files found in '{folder_path}'. Please select a different folder.")
            continue
        pdf_dir = os.path.join(folder_path, "pdf")
        docx_dir = os.path.join(folder_path, "word")
        txt_dir = os.path.join(folder_path, "txt")
        os.makedirs(pdf_dir, exist_ok=True)
        os.makedirs(docx_dir, exist_ok=True)
        os.makedirs(txt_dir, exist_ok=True)
        for epub_file in epub_files:
            convert_epub(epub_file, pdf_dir, docx_dir, txt_dir)
        print("\n" + "="*50)
        print("Folder conversion complete.")
        print("="*50)

if __name__ == "__main__":
    main()