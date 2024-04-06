# Easy hash calculator

This is a simple-executable for calculating hash checksums.

# Available algorithm

SHA1/256/384/512<br>
MD5<br>
...(To be continued......)

# Usage

1. Install `pyinstaller` with pip by code under:

   `pip install pyinstaller`

2. Build

   `pyinstaller -F -y pyhashcalc.py`

3. Move into `C:\Windows`
Builded executable can be found in .\dist folder.

4. Type command under in any terminal.
   `pyhashcalc <algorithm> <filename> [copy] [upper]`
   if copy, the result will be copy.
   if upper, the result will be uppercase.

# Caution: This project is only support Windows!!!!

