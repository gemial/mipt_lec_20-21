def create_russ_doll(n:int):
    if n == 1:
        print('сделал матрёшку')
        return
    print('Верх матрёшки', n)
    create_russ_doll(n-1)
    print('Низ матрёшки', n)

create_russ_doll(5)
