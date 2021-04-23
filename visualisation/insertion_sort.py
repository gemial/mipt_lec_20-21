#!/usr/bin/python

import vis
from random import randint

A = list([randint(10, 99) for _ in range(10)])


print('Start :', A)
for i in range(1, len(A)):
    j = i
    while j > 0 and A[j - 1] > A[j]:
        A[j], A[j - 1] = A[j - 1], A[j]
        j -= 1
    print('Step  :', A)
print('Stop  :', A)
