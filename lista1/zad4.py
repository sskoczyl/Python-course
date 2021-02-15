import math

def primeFactors(n):
    factors=[]
    counter=0

    while n % 2 == 0: 
        counter+=1
        n = n / 2

    if(counter>0):
        factors.append("(2, "+str(counter)+")")
           
    for i in range(3,int(math.sqrt(n))+1,2): 
        counter=0

        while n % i== 0: 
            counter+=1 
            n = n / i 

        if(counter>0):
            factors.append("("+str(i)+", "+str(counter)+")")

    if n > 2: 
        factors.append("("+str(n)+", "+str(1)+")")

    return factors    



n=input("Podaj liczbę całkowitą:" )
print("Rozkład na czynniki pierwsze:", primeFactors(int(n)))