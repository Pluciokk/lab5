def poletrojkata():
    a = int(input("Podaj bok a : "))
    b = int(input("Podaj bok b : "))
    c = int(input("Podaj bok c : "))
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and c+b>a:
            p = (a + b + c) / 2
            P = (p*(p-a)*(p-b)*(p-c))**(1/2)
            print("Pole trojkata wynosi:", P)
        else:
            print("Podano niepoprawna dlugosc boku")
    else:
        print("Podano niepoprawna dlugosc boku")

poletrojkata()
