def hanoy(n, i=1, j=2):
    if n == 1:
        print(f'Переложить с {i} на {j}')
        return
    hanoy(n-1, i, 6-i-j)
    print(f'Переложить с {i} на {j}')
    hanoy(n-1, 6-i-j, j)
    
hanoy(6)
