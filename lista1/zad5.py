def faczero(num):
    factorial = 1
    counter=0

    if(0>num or num>1000):
        raise Exception("Error")
    elif num == 0:
        return 0
    else:
        for i in range(1,num + 1):
            factorial = factorial*i

    while(factorial%10==0):
        factorial=factorial//10
        counter+=1

    return counter 

num=input("Podaj nieujemną liczbę całkowitą: ")
try:
    print("Liczba zer na koncu:", faczero(int(num)))
except:
    print("Podana liczba musi byc calkowita i nalezec do zakresu 0-1000")