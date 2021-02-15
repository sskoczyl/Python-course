import math
import random
import timeit


def iexp(n):
    return complex(math.cos(n), math.sin(n))


def fft_recur(arr, n, start=0, hop=1):
    if n == 1:
        return [arr[start]]

    cnt = n // 2
    tmp = fft_recur(arr, cnt, start, hop * 2) + fft_recur(arr, cnt, start + hop, hop * 2)

    for i in range(cnt):
        e = iexp(-2 * math.pi * i / n)
        tmp[i], tmp[i + cnt] = tmp[i] + e * tmp[i + cnt], tmp[i] - e * tmp[i + cnt]

    return tmp


def ifft_recur(arr, n, start=0, hop=1):
    if n == 1:
        return [arr[start]]

    cnt = n // 2
    tmp = ifft_recur(arr, cnt, start, hop * 2) + ifft_recur(arr, cnt, start + hop, hop * 2)

    for i in range(cnt):
        e = iexp(2 * math.pi * i / n)
        tmp[i], tmp[i + cnt] = tmp[i] + e * tmp[i + cnt], tmp[i] - e * tmp[i + cnt]

    return tmp


def my_fft(arr):
    return fft_recur(arr, len(arr))


def my_ifft(xs):
    return [v / len(xs) for v in ifft_recur(xs, len(xs))]


def create_vector(number, n):
    output = []

    for i in range(0, len(number)):
        idx = len(number) - i - 1
        output.append(int(number[idx]))

    while len(output) != 2 * n:
        output.append(0)

    return output


def number_from_vector(number):
    output = 0

    for idx, elem in enumerate(number):
        output += int(elem) * 10 ** idx

    return output


class FastBigNum:

    def __init__(self, num):
        num.replace('\u200b', '')
        self.number = num

    def __mul__(self, other):

        if len(self.number) > len(other.number):
            n=len(self.number)
        else:
            n = len(other.number)

        x = self.number
        y = other.number

        x = create_vector(x, n)
        y = create_vector(y, n)

        x = my_fft(x)
        y = my_fft(y)

        z = []
        for i in range(2 * n):
            z.append(complex(x[i] * y[i]))

        z = my_ifft(z)

        for i in range(2 * n):
            z[i] = int(round(z[i].real))

        num = number_from_vector(z)

        return FastBigNum(str(num))

    def __str__(self):
        return str(self.number)


A = '9999999999999999'  # '1312312231232131231231231231231231212331233231349'
B = '1024857600070000'  # '1212312311223123121312312321321231231112323123231'

a = FastBigNum(A)  # Ta implementacja działa tylko dla liczb o długości będącą potęgą 2
b = FastBigNum(B)

val = a * b
print(val)
print(int(A) * int(B))

"""""
start = timeit.timeit()
a*b
end = timeit.timeit()
print("FFT COOLNEY-TUKEY:",end - start)

start = timeit.timeit()
int(A)*int(B)
end = timeit.timeit()
print("ZWYKŁE *",end - start)
"""
