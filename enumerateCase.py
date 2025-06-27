l = [(1,2), (3,4)]
for e in l:
    print(e)


for e in l:
    a, b = e
    print(a)
    print(b)
    print("*****")

print("***********************")

for a,b in l:
    print("tuple ilk eleman:" , a)
    print("tuple ikinci eleman", b)
    print("--------------------------------")

adlar = ["emre","taha","nergis"]
for i, e in enumerate(adlar, start = 1):
    print(i, "indexteki eleman", e)