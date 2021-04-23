def find_left_bound(a: list, value:int) -> int:
    ''' find left bound of `value` in `a` '''
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (right + left) // 2
        if a[middle] < value:
            left = middle
        else:
            right = middle

    return left

def find_right_bound(a: list, value:int) -> int:
    ''' find left bound of `value` in `a` '''
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (right + left) // 2
        if a[middle] <= value:
            left = middle
        else:
            right = middle

    return right

a = [i*i for i in range(10)]
print(find_left_bound(a, 21))
print(find_left_bound(a, -4))
print(find_left_bound(a, 10000))
print(find_left_bound([1, 2, 3, 4, 4, 5, 8, 9], 4))

print(find_right_bound(a, 21))
print(find_right_bound(a, -4))
print(find_right_bound(a, 10000))
print(find_right_bound([1, 2, 3, 4, 4, 5, 8, 9], 4))

