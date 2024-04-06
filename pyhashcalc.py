import sys
import hashlib
import pyperclip
import io

def _raise_error_when_calculater_not_found(k):
    raise KeyError("Calculater for %s is not avaliable." % k)

calculater_list = {
    "sha256": hashlib.sha256, 
    "sha1": hashlib.sha1, 
    "sha384": hashlib.sha384, 
    "md5": hashlib.md5, 
    "sha512": hashlib.sha512
}

if len(sys.argv) in (1, 2):
    print("""ERROR: please enter the file name.
          
Usage: pyhashcalc [Calculater] [FileName] (upper) (copy)
Available hash calculater: %s
Use copy options to copy to clipboard.
Use upper options to display uppered result.
""" % list(calculater_list.keys()))
    sys.exit(1)

calculater_name = sys.argv[1].lower()

if calculater_name == "help":
    print("""Available hash calculater: %s
Use copy options to copy to clipboard.
Use upper options to display uppered result.""" % list(calculater_list.keys()))
    sys.exit(0)
    
    
calculater = calculater_list.get(calculater_name)
if calculater == None:
    _raise_error_when_calculater_not_found(calculater_name)

filename = sys.argv[2]

copy_to_clipboard = "copy" in sys.argv

upper = "upper" in sys.argv

with io.open(filename, "rb") as file:
    content = file.read()
    hashobj = calculater(content)
    hash_result = hashobj.hexdigest()
    if upper:
        hash_result = hash_result.upper()
    
    print(hash_result)
    if copy_to_clipboard:
        print("Success copied to clipboard.")
        pyperclip.copy(hash_result)
        

