
def bin_solve(f, left:float, right:float, epsilon = 0.0000001):
    ''' solve equation f(x) = 0 on [left, right] '''
    while right - left > epsilon:
        middle = (left + right) / 2
        if f(middle) == 0:
            return middle
        if f(left) * f(middle) < 0:
            right = middle
        else:
            left = middle

    
    return (right + left) / 2
        
from math import sin, pi

print(bin_solve(sin, 3, 4))
print(pi)
