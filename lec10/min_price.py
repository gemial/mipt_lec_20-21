from random import randint

def min_prices(N, price:list) -> list:
    res = [float("+inf"), price[0]] + [0] * (N-1)
    for i in range(2, N + 1):
        res[i] = price[i-1] + min(res[i-1], res[i-2])

    return res

def min_path(min_prices:list, prices:list) -> list:
    path = []
    i = len(prices)
    while i != 1:
        path.append(i)
        if min_prices[i-1] == min_prices[i] - prices[i-1]:
            i = i - 1
        else:
            i = i - 2
    
    return ([1] +  
           [path[i] for i in range(len(path) - 1, -1, -1)])

N = 10
prices = [randint(2, 10) for _ in range(N)]
print(prices)
minp = min_prices(N, prices)
print(minp)
print(min_path(minp, prices))

