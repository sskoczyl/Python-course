import sys
import os
import re

def decode(source, path):
    chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    binarycoded=""
    decoded=""

    with open(source) as f:
        encoded= f.read()
        
    for char in encoded:
        if char in chars:
            binary = bin(chars.index(char)).lstrip("0b")
            binary = (6-len(binary))*"0" + binary
            binarycoded += binary

    brackets = re.findall('(\d{8})', binarycoded)

    for bracket in brackets:
        decoded+=chr(int(bracket,2))
 
    with open(path, "a") as out:   
        out.truncate(0)  
        out.write(decoded)
        

def encode(source, path):
    chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    padding=0
    binarycoded=''
    base64_str=""

    with open(source) as f:
        text= f.read()
        
    for char in text:
        binary = bin(ord(char)).lstrip("0b")
        binary = (8-len(binary))*"0"+binary
        binarycoded += binary

    while (((len(text)) % 3) != 0):
	    binarycoded += "00000000"	
	    text += "0"
	
    brackets = re.findall('(\d{6})', binarycoded)

    for bracket in brackets:
    	if(bracket=="000000"):
    		base64_str+="="
    	else:
    		base64_str+=chars[int(bracket,2)]

 
    with open(path, "a") as out:
        out.truncate(0)   
        out.write(base64_str)


operation=sys.argv[1]
path_source=sys.argv[2]
path_target=sys.argv[3]

if(operation=='--encode'):
    encode(path_source, path_target)
elif(operation=='--decode'):
    decode(path_source, path_target)
else:
    print('Unknown operation, please try again')