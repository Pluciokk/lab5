def fibonacci(n):
    if n <= 0:
        return "Podaj liczbę naturalną większą od zera"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numer_wyrazu = int(input('Podaj numer wyrazu ciągu Fibonacciego: '))
wynik = fibonacci(numer_wyrazu)
print(f'{numer_wyrazu}-ty wyraz ciągu Fibonacciego to: {wynik}')
