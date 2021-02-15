import math
from math import *

def printMatrix(matrix):
    for y in range(0, 24):
        for x in range(0, 80):
            print(matrix[y][x], end = '')
        print()

def generateMatrix(function, a, b):
    matrix = [[' ' for x in range(80)] for y in range(24)]
    xratio = (abs(eval(b))+abs(eval(a)))/80
    max=0
    min=0
    a=eval(a)

    for y in range(0, 24):
        for x in range(0, 80):
            if(y==12):
                matrix[y][x]="-"
            if(x==40):
                matrix[y][x]="|"
    
    for x in range(0, 80):
        y_val=eval(function.replace("x", str(float(a)+xratio*x)))
        if(y_val>max):
            max=y_val
        elif(y_val<min):
            min=y_val
        

    if(abs(max)<abs(min)):
        yratio=2*round(abs(min))/24
    else:
        yratio=2*round(abs(max))/24

    for x in range(0, 80):
        if(eval(function.replace("x", str(float(a)+xratio*x)))>=0):
            outcome=round(abs(eval(function.replace("x", str(float(a)+xratio*x)))/yratio))
            outcome=outcome+(-2*outcome+12)
        else:
            outcome=round(abs(eval(function.replace("x", str(float(a)+xratio*x)))/yratio))+11

        matrix[outcome][x]='*'
     
    return matrix
       

function=input("Podaj funkcje f(x)=")
a=input("Podaj poczatek przedzialu a=")
b=input("Podaj koniec przedzialu b=")
matrix=generateMatrix(function, a, b)
printMatrix(matrix)


