def potega(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * potega(a, n - 1)
    else:
        return 1 / (a * potega(a, -n - 1))

a = int(input('Podaj podstawę potęgi: '))
n = int(input('Podaj wykładnik potęgi: '))

wynik = potega(a, n)
print(f'{a}^{n} = {wynik}')
