def square(x):
    return x*x

sonuc = square(3)
print(sonuc)


def power(x,y):
    return x**y

sonuc = power(2,3)
print(sonuc)


def fakHesapla(x):
    fak = 1
    for i in range(1, x + 1):
        fak *= i
    return fak

print(fakHesapla(5))

def fakHesapla(x):
    if x < 0:
        return "Negatif sayıların faktöriyeli yoktur."
    elif x == 0 or x == 1:
        return 1
    else:
        return x * fakHesapla(x - 1)
print(fakHesapla(-1))
