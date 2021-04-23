from random import randint

def bubble_sort(A:list):
    ''' make bubble sort of list A '''
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            

A = [randint(10, 99) for _ in range(15)]
print(A)
bubble_sort(A)
print(A)
