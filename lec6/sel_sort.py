from random import randint

def sel_sort(A:list):
    ''' Selection sort of list A'''
    for i in range(len(A) -1):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]

A = [randint(10, 99) for _ in range(15)]
print(A)
sel_sort(A)
print(A)

