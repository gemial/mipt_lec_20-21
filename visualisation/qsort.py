import vis
vis.VisualList.delay = 0.1
from random import random


def qsort(A, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(A) - 1
    if left >= right:
        return
    i, j = left, right
    while i < j:
        while i < j and A[i] < A[right]:
            i += 1
        while i < j and A[j] >= A[right]:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[i], A[right] = A[right], A[i]
    qsort(A, left, i - 1)
    qsort(A, i + 1, right)


A = list([random() for _ in range(12)], format='5.2')
print(A)
qsort(A)
print(A)
