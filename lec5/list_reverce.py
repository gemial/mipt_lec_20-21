def list_reverce(A:list, N:int):
    ''' Разворачивает список `A` с конца (N-1) до начала '''
    
    for i in range(N // 2):
        A[i], A[N-1-i] = A[N-1-i], A[i]

def test():
    n = 10
    A = list(range(n))
    print(A)
    list_reverce(A, n)
    print(A)
    if A == list(range(n-1, -1, -1)):
        print('Работает !!!')
    else:
        print('НЕ РАБОТАЕТ (((')

test()
