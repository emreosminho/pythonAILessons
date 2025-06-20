isim = "Emre"
print(isim[1])
print(isim[0:4])
print(isim[-1])
# print(isim[4]) hata alırım.
# isim[1] = "a"  # hata alırım çünkü stringler immutable'dır.
print(isim[0:4:2])  # 0'dan 4'e kadar 2'şer atlayarak alır.

sliceDeneme = "Python Programlama Dilimnjh"
print(sliceDeneme[0:50:5])
print(sliceDeneme[:])
print(sliceDeneme[0:5:2])
print(sliceDeneme[0:-1]) # -1 son karakteri almaz.
print(sliceDeneme[:0:-1])  # Ters çevirir.
print(sliceDeneme[::-1])   # Tüm stringi ters çevirir.