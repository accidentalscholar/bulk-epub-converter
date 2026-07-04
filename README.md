# Bulk EPUB Converter

This simple script converts all *EPUB* files found in a folder into *PDF*, *DOCX* and *TXT* in one go.

All the magic is done by standard *Python* libraries, *PyMuPDF* and *python-docx*, with this script adding just the specific workflow and interface.

## The Problem

There are plenty of tools to convert *EPUB* files into various formats. However, these usually work on a file-by-file basis, making the process labour-intensive and time-consuming.

This script converts all *EPUB* files in a folder in a single run. Further, it converts each file into *PDF*, *Word DOCX* and *TXT* text formats.

## Usage

### Preparation

Before using this script, ensure all the *EPUB* files you need to convert are stored in a single folder.

### Running the script

When you run the Python script, it will pop up a file explorer/finder window asking you to select the target folder.

Once you have done that, it will work through the conversions in the background. 

Once the conversions are completed, it will pop up the file explorer/finder window again, allowing you to select another target folder if you have more *EPUB* files to convert.

### Output

The *PDF* files are saved in a subfolder *pdf*, *Word DOCX* files in *word* and *TXT text* files in *txt*.

### Note

1. The script uses some standard *Python* libraries. If you don't have them installed on your system, then in the first run, the script will try to install these dependencies. If the script can't install these dependencies, for instance if your PC environment precludes it, then it will usually give you the console commands you can use to install these.
2. If some of your libraries and executables sit outside the *Path*, such as if you don't have Admin rights to your work laptop, then you should include the folder addresses in the 'path.txt' file, which should sit in the same folder as the '*bulk-epub-converter.py*' file, e.g. '*C:\Users\Username\AppData\Roaming\Python\Python313\Scripts*' and '*C:\Users\Username\AppData\Roaming\Python\Python313\site-packages*'.

## Caveat

Tested on *Windows 11 Education 64-bit*.

Not tested on *Apple iOS* or *Linux*.

## Never run a Python script before?

It's straightforward, but you may need to install *Python* on your machine first.

### Install Python

*Anaconda* is one of the most popular distributions of *Python*. Download and install from https://www.anaconda.com/download

Installation is simple, but if you need help, check out https://www.anaconda.com/docs/getting-started/anaconda/install/overview

### Start Spyder

*Anaconda* comes with *Spyder IDE*. Start *Spyder*.

Once *Spyder* is ready, open the file 'bulk-epub-converter.py' that has the script.

All that's left is for you to hit 'Run', i.e. the green 'Play' button.