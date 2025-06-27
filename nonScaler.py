notlar = [80,80,80,80]

toplam = 0
for e in notlar:
    toplam += e
    ortalama = toplam/len(notlar)
print(ortalama)



d = {"Emre":85, "Taha":65}

for i in d:
    value = d[i]

    if value > 66:
        print(i)
