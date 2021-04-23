def gen(n, prefix=None, used=None):
    if prefix is None:
        prefix = []
        used = [False] * n
    if n == 0:
        print(''.join(map(str, prefix)), end=' ')
        return
    for i in range(len(used)):
        if not used[i]:
            used[i] = True
            prefix.append(i)
            gen(n-1, prefix, used)
            prefix.pop()
            used[i] = False

gen(5)
        
