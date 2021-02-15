import os
import sys

def getSize(path):
    return os.path.getsize(path)


def getWords(path):
    file=open(path)
    data=file.read()
    words=data.split()
    file.close()
    return len(words)
    

def getLines(path):
    num_lines=0
    file=open(path)
    with file as f:
        for line in f:
            num_lines+=1

    file.close()
    return num_lines


def getMaxLine(path):
    file=open(path)
    lines_count=len(max(file, key=len))
    file.close()
    return lines_count


path=sys.argv[1]

try:
    print("Bytes:", getSize(path))
    print("Word count:", getWords(path))
    print("Line count:", getLines(path))
    print("Max line:", getMaxLine(path))
except:
    print('Nieprawidlowa sciezka do pliku!')