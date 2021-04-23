#!/usr/bin/python

from random import randint, shuffle
import vis
vis.VisualList.delay /= 2



def fool_sort(X):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(X)):
            if X[i - 1] > X[i]:
                X[i - 1], X[i] = X[i], X[i - 1]
                sorted = False
                break



a = list([randint(0, 10000) for _ in range(10)])
print('Start :', a)
fool_sort(a)
print('End   :', a)
