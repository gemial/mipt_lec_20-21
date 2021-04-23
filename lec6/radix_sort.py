#!/usr/bin/python

from random import randint
import math
import sys

def mystr(y, x):
    y = f'{y:04}'
    x = math.ceil(math.log(x, 10))

    if len(sys.argv) > 1:
            return f'\033[0m{y[:-x]}\033[44m{y[-x:]}\033[0m'

    if x == 1:
        return f'\033[0m{y[:-x]}\033[44m{y[-x]}\033[0m'
    return f'\033[0m{y[:-x]}\033[44m{y[-x]}\033[0m{y[-x+1:]}'


def rsort2(X):
    x = 1
    while x < 10000:
        A = []
        B = []
        for el in X:
            if not x & el:
                A.append(el)
            else:
                B.append(el)

        X.clear()
        X.extend(A)
        X.extend(B)
        x <<= 1


def rsort10(X):
    x = 1
    while x < 10000:
        A = [[] for _ in range(10)]
        for el in X:
            A[el // x % 10].append(el)
        X.clear()
        for ar in A:
            X.extend(ar)
        x *= 10

        print('\t'.join(map(lambda y: mystr(y, x) , X)))

a = [randint(100, 10000) for _ in range(10)]
print('\t'.join(map(str, a)))
rsort10(a)
print('\t'.join(map(str, a)))
