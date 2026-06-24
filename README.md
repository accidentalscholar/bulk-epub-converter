# Bulk EPUB Converter

This simple script converts all _EPUB_ files found in a folder into _PDF_, _DOCX_ and _TXT_ in one go.

All the magic is done by standard _Python_ libraries, _PyMuPDF_ and _python-docx_, with this script adding just the specific workflow and interface.

## The Problem

There are plenty of tools to convert _EPUB_ files into various formats. However, these usually work on a file-by-file basis, making the process labour-intensive and time-consuming.

This script converts all _EPUB_ files in a folder in a single run. Further, it converts each file into _PDF_, _Word DOCX_ and _TXT_ text formats.

## Usage

### Preparation

Before using this script, ensure all the _EPUB_ files you need to convert are stored in a single folder.

### Running the script

When you run the Python script, it will pop up a file explorer/finder window asking you to select the target folder.

Once you have done that, it will work through the conversions in the background. 

Once the conversions are completed, it will pop up the file explorer/finder window again, allowing you to select another target folder if you have more _EPUB_ files to convert.

### Output

The _PDF_ files are saved in a subfolder _pdf_, _Word DOCX_ files in _word_ and _TXT text_ files in _txt_.

### Note

1. The script uses some standard _Python_ libraries. If you don't have them installed on your system, then in the first run, the script will try to install these dependencies. If the script can't install these dependencies, for instance if your PC environment precludes it, then it will usually give you the console commands you can use to install these.
2. If some of your libraries and executables sit outside the _Path_, such as if you don't have Admin rights to your work laptop, then you should include the folder addresses in the 'path.txt' file, which should sit in the same folder as the 'timetable_drafter.py' file, e.g. 'C:\Users\Username\AppData\Roaming\Python\Python313\Scripts' and 'C:\Users\Username\AppData\Roaming\Python\Python313\site-packages'.

## Caveat

Tested on _Windows 11 Education 64-bit_.

Not tested on _Apple iOS_ or _Linux_.

## Never run a Python script before?

It's straightforward, but you may need to install _Python_ on your machine first.

### Install Python

_Anaconda_ is one of the most popular distributions of _Python_. Download and install from https://www.anaconda.com/download

Installation is simple, but if you need help, check out https://www.anaconda.com/docs/getting-started/anaconda/install/overview

### Start Spyder

_Anaconda_ comes with _Spyder IDE_. Start _Spyder_.

Once _Spyder_ is ready, open the file 'bulk_epub_converter.py' that has the script.

All that's left is for you to hit 'Run', i.e. the green 'Play' button.