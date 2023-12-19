def trapez():
    a = int(input("Podaj podstawe a : "))
    b = int(input("Podaj podstawe b : "))
    h = int(input("Podaj wysokosc h : "))
    print(((a+b)*h)/2)

#trapez()

def trapez2():
    a = int(input("Podaj podstawe a : "))
    b = int(input("Podaj podstawe b : "))
    h = int(input("Podaj wysokosc h : "))
    p = ((a+b)*h)/2
    return p

print(trapez2())