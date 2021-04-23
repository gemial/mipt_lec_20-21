#!/usr/bin/python

import vis
from random import randint
vis.VisualList.delay = 0.01

A = list([randint(10, 99) for _ in range(10)])

start = 0
end = len(A) - 1

print('Start :', A)
sorted = False
while not sorted:
    sorted = True
    for j in range(start, end):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            end = j
            if sorted:
                start = max(0, j - 1)
            sorted = False
    print('Step  :', A)
print('Stop  :', A)
