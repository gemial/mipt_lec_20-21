def list_search(A:list, N:int, x:int) -> bool:
    '''Поиск элемента `x` в массиве `A` среди 
       первых `N` элементов.
       Результат - True, если есть. Иначе False'''

    for i in range(N):
        if A[i] == x:
            return True

    return False


def test_1():
    a = [1, 5, 8, -9, 17]
    if list_search(a, 5, -9):
        print('Работает ')
    else:
        print("Не работает")


test_1()

