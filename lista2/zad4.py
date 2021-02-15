import hashlib 
from collections import defaultdict
import os
import sys

def hashing(file):
    hash = hashlib.md5()
    with open(file, "rb") as f:
        chunk = f.read(1024)
     
        while chunk:
            hash.update(chunk)
            chunk = f.read(1024)

    return hash.hexdigest()


folder=arg = sys.argv[1]
hashcodes = defaultdict(list)

for path, dirs, files in os.walk(folder):
    for file in files:
        file_path = os.path.join(os.path.abspath(path), file)
        hashcodes[hashing(file_path)].append(file_path)

duplicate = (val for key, val in hashcodes.items() if len(val) > 1)

for file in duplicate:
    print(file)