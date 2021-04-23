#!/usr/bin/python

import vis
from random import randint

A = list([randint(10, 99) for _ in range(10)])


print('Start :', A)
for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
        str(A)
    print('Step  :', A)
print('Stop  :', A)
