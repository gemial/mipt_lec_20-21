from random import randint
def grash(n, allowed:list)->int:
    ''' calculate number of variants of ways for grasshopher
        jumps from first grass to `n`
        allowed - list of allwed for jump '''
    res = [1] + [0] * (n - 1)
    for i in range(n-1):
        for j in range(1, 4):
            if i+j < n and allowed[i+j]:
                res[i+j] += res[i]

    return res[n-1]

N = 10  
allowed = [True] * N

allowed[randint(2,8)] = False
print(allowed)
print(grash(N, allowed))
