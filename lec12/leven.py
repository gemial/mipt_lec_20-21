
def edit_dist(s:str, g:str):
    ''' calculate Levenshtain distanse between strings
    >>> edit_dist('moloko', 'kolobok')
    3
    >>> edit_dist('abc', 'abc')
    0
    >>> edit_dist('kolobok', 'korobok')
    1
    >>> edit_dist('', 'asdasd')
    6
    '''
    
    F = [[ i+j if i*j == 0 else 0 for i in range(len(g)+1) ]
          for j in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(g) + 1):
            if s[i-1] == g[i-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i][j-1], F[i-1][j-1], F[i-1][j]) + 1 

    return F[len(s)][len(g)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
