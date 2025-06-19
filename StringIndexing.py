isim = "Emre"
print(isim[1])
print(isim[0:4])
print(isim[-1])
# print(isim[4]) hata alırım.
# isim[1] = "a"  # hata alırım çünkü stringler immutable'dır.
print(isim[0:4:2])  # 0'dan 4'e kadar 2'şer atlayarak alır.

sliceDeneme = "Python Programlama Dilimnjh"
print(sliceDeneme[0:-1:5])
print(sliceDeneme[:])