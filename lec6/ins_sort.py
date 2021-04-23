from random import randint

def ins_sort(A:list):
    '''insertion sort of A'''
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1

A = [randint(10,99) for _ in range(15)]
print(A)
ins_sort(A)
print(A)
