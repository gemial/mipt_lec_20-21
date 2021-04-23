
def gos(A:list, B:list):
    m = [[0] * (len(B) + 1) for _ in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                m[i][j] = m[i-1][j-1] + 1
            else:
                m[i][j] = max(m[i-1][j], m[i][j-1])

    return m

def get_sequense(A:list, B:list, m):
    i = len(A)
    j = len(B)
    while i > 0 and j > 0:
        if m[i][j] - m[i-1][j-1] == 1:
            print(A[i-1], end='\t')
            i -= 1
            j -= 1
        else:
            if m[i-1][j] == m[i][j]:
                i -= 1
            else:
                j -= 1
A = [1, 5, 2, 8, 3, 2]
B = [1, 0, 2, 3, 7, 2, -20]
res = gos(A,B) 

for line in res:
    for element in line:
        print(element, end='\t')
    print()
get_sequense(A, B, res)

