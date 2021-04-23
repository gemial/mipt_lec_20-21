start, stop, step = 0, 100, 3

x = start
while x < stop:
    print(x)
    x += step

for x in range(start, stop, step):
    print(x)

for x in (1, 3, 8, 'abc'):
    print(3*x)

