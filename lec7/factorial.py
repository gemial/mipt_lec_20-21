def fact(n:int)->int:
    if n < 0:
        raise ValueError(f'Can\'t calculate ({n})!')
    if n == 0:
        return 1

    return fact(n-1) * n

print(fact(997))
print(fact(998))

