def factor(x:int):
    ''' Print factor of number x'''
    if type(x) is not int or x <= 0:
        return float('nan')
    
    curr = 2
    while curr < x:
        if x % curr == 0:
            print(curr, end=' ')
            x //= curr
        else:
            curr += 1 
   
    print(x)

factor(1231230)
