def list_shift(A:list, N:int):
    ''' Сдвигаем список на один элемент влево '''

    tmp = A[n-1]
    for i in range(N-1, 0, -1):
        A[i] = A[i-1]

    A[0] = tmp

n = int(input())
A = input().split()
list_shift(A, n)
print(A)

