def pref(s:str):
    res = [0 for _ in s]
    for i in range(1, len(s)):
        p = res[i - 1]
        while p != 0 and s[p] != s[i]:
            p = res[p]
        if s[i] == s[p]:
            res[i] = p + 1
        else:
            res[i] = 0
    return res

s = 'abacabadabacabafabacabada'
print(*s, sep='  ')
print(*pref(s), sep='  ')



def kmp(substr, string):
    '''search substring in string
    >>> kmp('abc', 'abc ddd abcabc d abc')
    0 8 11 17 
    >>> kmp('abc', 'adsffqwetgerhtyh')
    
    >>> kmp('qwe', '123qwe123')
    3 
    '''
    s = substr + '\0' + string
    res = pref(s)
    
    for i in range(len(substr), len(res)):
        if res[i] == len(substr):
            print(i - 2 * len(substr), end=' ')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
