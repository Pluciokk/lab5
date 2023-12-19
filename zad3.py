def PoleTr():
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    if a+b>c and a+c>b and c+b>a:
        p = (a+b+c)/2
        P = (p*(p-a)*(p-b)*(p-c))**(1/2)
        print(P)
    else:
        print("Nie poprawny trójkąt")

PoleTr()
