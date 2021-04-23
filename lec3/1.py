x = int(input('Введите число '))
y = int(input('Основание '))

res = ''
while x != 0:
    res = str(x % y) + res
    x //= y

print(res)
