for i in range(5):
    print(i)
# Bu kod, 0'dan 4'e kadar olan sayıları yazdırır.

for i in range(0, 100, 5):
    print(i)


x = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz: "))
for i in range(x+1):
    if i == 0:
        fak = 1
    else:
        fak *= i
print("Faktöriyel:", fak)

for i in range (0,10,2):
    print(i)

y = int(input("Faktoriyel alinacak sayiyi giriniz:"))
faktoriyel = 1
for i in range (y+1):
    if i != 0:
        faktoriyel *= i
print(faktoriyel)
