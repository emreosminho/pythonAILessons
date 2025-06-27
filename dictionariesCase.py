isim = ["emre", "nergis", "taha"]
notlar = [65,95,85]
print(isim[0], "adlı ogrencinin notu", notlar[2])



isimNot = {"Emre":85, "Nergis":95, "Taha":65}
print(isimNot["Emre"])

ogrenciler = {"Emre":{"no":808, "not":85}, "Taha":{"no":809, "not":95}}
print(ogrenciler["Emre"])
print(ogrenciler["Taha"])
print(ogrenciler["Taha"]["not"])
