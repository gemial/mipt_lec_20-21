def is_simple(x: int) -> bool:
    ''' Return True if x is a simple number
        Else return False
        Wrong data return Nan'''
    if type(x) is not int or x <= 0:
        return float('nan')
    
    for i in range(2, x):
        if x % i == 0:
            return False

    return True

last = int(input())
i = 0
j = 2
while i < last:
    if is_simple(j):
        i += 1
    j += 1

print(j - 1) 
