import math
from math import *

def checkInput(formula):
    return formula.replace('^','**')

try:
    formula=input("Wprowadz wyrazenie: ")
    print(formula+"=",eval(checkInput(formula)))
except:
    print("Cos poszlo nie tak, wprowadzac mozna tylko \nliczby i standardowe operacje matematyczne")
