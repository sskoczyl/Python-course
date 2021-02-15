import random
import timeit
from cmath import exp
from math import pi


def omega(k, n):
    return exp(-2j * k * pi / n)


def dft(x, n):
    return [sum(x[i] * omega(i * k, n) if i < len(x) else 0 for i in range(n)) for k in range(n)]


def idft(x, n):
    return [int(round(sum(x[i] * omega(-i * k, n) if i < len(x) else 0 for i in range(n)).real) / n) for k in range(n)]


def number_from_vector(number):
    output = 0

    for idx, elem in enumerate(number):
        output += int(elem) * 10 ** idx

    return output


def create_vector(number, n):
    output = []

    for i in range(0, len(number)):
        idx = len(number) - i - 1
        output.append(int(number[idx]))

    while len(output) != 2 * n:
        output.append(0)

    return output


class FastBigNum:

    def __init__(self, num):
        num.replace('\u200b', '')
        self.number = num

    def __mul__(self, other):

        if len(self.number) > len(other.number):
            n = len(self.number)
        else:
            n = len(other.number)

        x = self.number
        y = other.number

        x = create_vector(x, n)
        y = create_vector(y, n)

        x = dft(x, len(x))
        y = dft(y, len(y))

        z = []
        for i in range(2 * n):
            z.append(complex(x[i] * y[i]))

        num = number_from_vector(idft(z, len(z)))
        return FastBigNum(str(num))

    def __str__(self):
        return str(self.number)


A = '1312312231232131231231231231231231212331233231349'
B = '1212312311223123121312312321321231231112323123231'
# A = ''.join([random.choice("0123456789") for i in range(100000)])
# B = ''.join([random.choice("0123456789") for i in range(100000)])
a = FastBigNum(A)
b = FastBigNum(B)

val = a * b * a * b
print(val)
print(int(A) * int(B) * int(A) * int(B))

"""""
start = timeit.timeit()
a*b
end = timeit.timeit()
print("FFT NAIWNE:",end - start)

start = timeit.timeit()
int(A)*int(B)
end = timeit.timeit()
print("ZWYKŁE *",end - start)
"""
