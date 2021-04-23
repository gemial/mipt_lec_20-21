from prefix import pref

def kmp(substr:str, string:str):
    ''' search positions of substring in string
    >>> kmp('abc', 'abc abc abc')
    0 4 8 
    >>> kmp('abc', 'r]qo[wier[hwert')
    
    >>> kmp('aba', 'abacabadabacabafabacabad')
    0 4 8 12 16 20 
    '''
    s = substr + '\0' + string
    res = pref(s)
    for i in range(2 * len(substr), len(s)):
        if res[i] == len(substr):
            print(i - 2 * len(substr), end=' ')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
