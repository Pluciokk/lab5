def pole(r):
    if r>0:
        print(3,14*(r*r))
    else:
        print("Podano niepoprawne dane")

r = float(input("Podaj promień : "))
pole(r)

def pole2(r2):
    if r2>0:
        r2 = float(input("Podaj promien:"))
        return 3.14 * r2 ** 2
    else:
        print("Podano niepoprawne dane")
def pole3():
    r = float(input("Podaj promien: "))
    p =3.14*r**2

    return p