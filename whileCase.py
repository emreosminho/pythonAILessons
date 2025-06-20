x = int(input("bir sayı giriniz: "))

while x < 0:
    print("Negatif sayı girdiniz. Lütfen pozitif bir sayı giriniz.")
    x = int(input("bir sayı giriniz: "))
print("Pozitif sayı girdiniz:", x)
# Bu kod, kullanıcıdan pozitif bir sayı girmesini ister. Eğer kullanıcı negatif bir sayı girerse, kullanıcıya 
# hata mesajı gösterir ve tekrar sayı girmesini ister.

x = int(input("bir sayı giriniz: "))
fak = 1
while x > 0:
    fak *= x
    x -= 1
# Bu kod, kullanıcının girdiği pozitif sayının faktöriyelini hesaplar.
print("Faktöriyel:", fak)