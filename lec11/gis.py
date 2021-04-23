from random import randint

def gis(A:list):
    Z = [0] * len(A)
    for i in range(len(A)):
        m = 0
        for j in range(i):
            if A[j] < A[i] and Z[j] > m:
                m = Z[j]
        Z[i] = 1 + m

    print(Z)
    m = Z[0]
    for a in Z:
        m = a if a > m else m
    return m

Z = [randint(11, 99) for _ in range(10)]
print(Z)
print(gis(Z)
)
