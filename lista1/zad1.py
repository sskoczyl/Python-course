
def printTriangle(n):

    for line in range(0, n):
        for s in range (0, n-line):
                print(" ", end = "")
        for i in range(0, line+1):
            print(binominal(line, i), " ", end = "")
        print()


def binominal(n, k):
    help=1
    if(k > n - 1):
        k=n-k
    for i in range(0, k):
        help = help * (n - i)
        help = help // (i +1)
    
    return help




n= input("Podaj wysokosc trojkata n= ")
printTriangle(int(n))