#!/usr/bin/python

from random import randint, shuffle
import vis
vis.VisualList.delay /= 50


def is_sorted(X):
    for i in range(1, len(X)):
        if X[i - 1] > X[i]:
            return False
    return True


def monkey_sort(X):
    while not is_sorted(X):
        shuffle(X)


a = list([randint(0, 10000) for _ in range(6)])
print('Start :', a)
monkey_sort(a)
print('End   :', a)
