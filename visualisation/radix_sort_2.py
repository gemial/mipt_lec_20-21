#!/usr/bin/python

from random import randint
import vis
vis.VisualList.delay /= 5


def rsort2(X):
    x = 1
    singles = list()
    zeros = list()
    while x < 10000:
        singles.clear()
        zeros.clear()

        for el in X:
            if el & x:
                singles.append(el)
            else:
                zeros.append(el)
        X.clear()
        X.extend(zeros)
        X.extend(singles)
        x <<= 1


a = list([randint(0, 10000) for _ in range(15)])
print(a)
rsort2(a)
print(a)
