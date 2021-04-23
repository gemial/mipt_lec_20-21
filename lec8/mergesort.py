from random import randint

def mergesort(A):
    if len(A) < 2:
        return 
    n = len(A) // 2
    B = list(A[0:n])
    C = list(A[n:])
    mergesort(B)
    mergesort(C)
    i = j = k = 0
    while not( i == len(B) and j == len(C)):
        if i == len(B):
            A[k] = C[j]
            j += 1
        elif j == len(C):
            A[k] = B[i]
            i += 1
        elif B[i] < C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
     
def merge(B,C):
    A = [0] * (len(B) + len(C))
    i = j = k = 0
    while i != len(B) or j != len(C):
        if i == len(B):
            A[k] = C[j]
            j += 1
        elif j == len(C):
            A[k] = B[i]
            i += 1
        elif B[i] < C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    return A

print(merge([1,3,5], [2,5,8]))

X = [randint(10, 99) for _ in range(15)]
print(X)
mergesort(X)
print(X)
