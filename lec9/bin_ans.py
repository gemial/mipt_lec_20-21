
n, m, N = map(int, input().split())

left = 0
right = (n + m) * N
while right - left > 1:
    middle = (right + left) // 2
    if (middle // n) * (middle // m) < N:
        left = middle
    else:
        right = middle

print(left + 1)
