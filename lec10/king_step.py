
def king_step(n):
    res = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==1 and j==1:
                res[i][j] = 1
            else:
                res[i][j] = res[i-1][j] + res[i][j-1]

    return res

A = king_step(8)
for line in A:
    for element in line:
        print('{:6}'.format(element), end='')
    print()
