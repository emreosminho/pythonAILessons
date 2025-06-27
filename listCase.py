notlar = [40,60,70,80,90]
print(notlar[0])
print(notlar[4])

# Farklı veri tipleri tutabiliyorum

listeKarma = ["a", "b", 50, 4.5, [5,6,9]]
print(listeKarma[4])
listeKarma[0] = 5            #mutable Elemanlar güncelleştirilebilmekte.
print(listeKarma[0])
print(listeKarma[1:])
print(listeKarma[:5222])

listeKarma.append(200) # sona ekler
print(listeKarma)

listeKarma.insert(0, 100) # başa ekler
print(listeKarma)

listeKarma.insert(3, 525252)
print(listeKarma)

listeKarma.remove(100)   #ilk gördüğü verdiğim elemanı siler
print(listeKarma)     