liste = ["Emre", "Canakci", 25, 1.75, True]
for i in liste:
    print(i)

print("Listenin 1. elemanı:", liste[0])


## Fonkssiyon olmadan faktöriyel hesaplama
sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz: "))
for i in range(1, sayi + 1):
    if i == 1:
        faktoriyel = 1
    else:
        faktoriyel *= i
print("Faktöriyel:", faktoriyel)

