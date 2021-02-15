def isPrime(n): 

    if (n <= 1): 
        return False
    if (n <= 3): 
        return True

    if (n % 2 == 0 or n % 3 == 0): 
        return False
  
    i = 5
    while(i*i<=n): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i=i+6
  
    return True

def primes(n):
    primes=[]

    for i in range(0,n):
        if( isPrime(i)):
            primes.append(i)

    return primes
    

n =input("Podaj liczbe calkowita: ")
print("Liczb pierwszych <"+n+" jest: ",primes(int(n)))