#!/usr/bin/python

from random import randint
import vis

def rsort10(X):
    x = 1
    A = [list() for _ in range(10)]
    while x < 10000:
        for ar in A:
            ar.clear()
        for el in X:
            A[el // x % 10].append(el)
        X.clear()
        for ar in A:
            X.extend(ar)
        x *= 10

a = list([randint(0, 10000) for _ in range(15)])
print(a)
rsort10(a)
print(a)
