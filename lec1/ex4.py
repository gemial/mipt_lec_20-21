x = 0
while True:
    if x%2 == 0:
        x += 1
        continue
    print(x)
    x += 1
    if x >=10:
        break
