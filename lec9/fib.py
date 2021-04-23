cache = [0, 1, 1]

def fib(n):
    if n < len(cache):
        return cache[n]
    cache.append(fib(n-2) + fib(n-1))
    return cache[n]


for i in range(40, 50):
    print(fib(i), end=' ')

print(' '.join(map(str, cache)))
