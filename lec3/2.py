s = input().encode()
y = int(input('Введите основание системы исчисления '))

res = 0

for ch in s:
    ch = ch - 48 if ch < 58 else ch - 55
    if ch >= y:
        print("WRONG NUMBER")
        break
    res  = res * y + ch

print(res)
