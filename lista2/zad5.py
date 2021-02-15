import random
from random import getrandbits
import sys
import math

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def xgcd(a, b):
    x, prevx = 0, 1
    y, prevy = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        prevx, x = x, prevx - quotient * x
        prevy, y = y, prevy - quotient * y

    return a, prevx, prevy

def chooseE(totient):
    while (True):
        e = random.randrange(2, totient)

        if (gcd(e, totient) == 1):
            return e

def isPrime(n, k):
    
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    s = 0
    r = n - 1

    while r & 1 == 0:
        s += 1
        r //= 2

    for i in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def genPrimeCandidate(length):
    p = getrandbits(length)
    return p

def genPrimeNumber(length):
    p = 4

    while not isPrime(p,length):
        p = genPrimeCandidate(length)
    return p

def randomPrimes(bits):
    length=int(math.log(2)/math.log(10)*bits)
    prime1=genPrimeNumber(length)
    prime2=genPrimeNumber(length)

    while prime2==prime1:
        prime2=genPrimeNumber(length)

    return prime1, prime2


def genKeys(bits):
   
    prime1, prime2 = randomPrimes(bits)

    n = prime1 * prime2
    phi = (prime1 - 1) * (prime2 - 1)
    e = chooseE(phi)

    gcd, x, y = xgcd(e, phi)

    if (x < 0):
        d = x + phi
    else:
        d = x
    with open('key.pub', "w") as f:
        f.write(str(n) + '\n')
        f.write(str(e) + '\n')
    with open('key.prv', 'w') as f:
        f.write(str(n) + '\n')
        f.write(str(d) + '\n')
        

def encrypt(message):

    with open('key.pub', 'r') as f:
        n = int(f.readline())
        e = int(f.readline())

    blocks = []
    codedtext = -1

    if (len(message) > 0):
        codedtext = ord(message[0])

    for i in range(1, len(message)):
        if (i % 2 == 0):
            blocks.append(codedtext)
            codedtext = 0
        codedtext = codedtext * 1000 + ord(message[i])

    blocks.append(codedtext)

    for i in range(len(blocks)):
        blocks[i] = str(pow(blocks[i],e,n))

    encrypted = " ".join(blocks)

    return encrypted

def decrypt(blocks):
    
    with open('key.prv', 'r') as f:
        n = int(f.readline())
        d = int(f.readline())
    blist = blocks.split(' ')
    numblocks = []

    for b in blist:
        numblocks.append(int(b))

    message = ""

    for i in range(len(numblocks)):
        numblocks[i] = pow(numblocks[i],d,n)
        tmp = ""

        for c in range(2):
            tmp = chr(numblocks[i] % 1000) + tmp
            numblocks[i] //= 1000
        message += tmp

    return message


if (sys.argv[1] == '--gen-keys'):
    genKeys(int(sys.argv[2]))
elif (sys.argv[1] == '--encrypt'):
    tocode=sys.argv[2]
    for i in range(3, len(sys.argv)):
        tocode+=" "+sys.argv[i]
    print(encrypt(tocode))
elif (sys.argv[1] == '--decrypt'):
    coded=sys.argv[2]
    for i in range(3, len(sys.argv)):
        coded+=" "+sys.argv[i]
    print(decrypt(coded))
else:
    print('That is not a proper instruction.')
