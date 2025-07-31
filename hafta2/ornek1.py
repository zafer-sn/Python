"""
isimSoyisim -> camelCase
isim_soyisim -> snake_case
İsimSoyisim -> PascalCase
"""
isimSoyisim = "Zafer SeaaaaERİN"
# len -> length -> uzunluk
print(isimSoyisim[10])
print(len(isimSoyisim))
print(isimSoyisim[len(isimSoyisim)-1]) # isimSoyisim[11]
print(f"Ters indis ile son harf: {isimSoyisim[-1]}")
# string slices
# start_index:stop_index:step_size
print(isimSoyisim)
print(isimSoyisim[::])
print(isimSoyisim[3::])
print(isimSoyisim[:7:])
print(isimSoyisim[::2])
print(isimSoyisim[::3])
print(isimSoyisim[1:7:3])
print(isimSoyisim[-10:-7:])
# ilgili stringi ters çevirir
print(isimSoyisim[::-1])
isim = "Ahmet"
soyisim = "DEMİR"
x = 3
y = 5
print(x + y)
# concat -> concatenate -> yan yana yaz
print(isim + " " + soyisim)
# print(isim - soyisim) -> hata
print(isim * 5)
# print(isim / 5) -> hata
# İlk harfi büyük diğerlerini küçük yapar
# print(isimSoyisim.capitalize())
# print(isimSoyisim.capitalize())
# İlk kelimelerin ilk harflerini büyük yapar.
print(isimSoyisim.title())
print(isimSoyisim.count("a")) # counter -> sayac
print(isimSoyisim.center(25, "*"))
bilecikPlaka = 11
print(isimSoyisim.endswith("N"))
print(isimSoyisim.index("e"))
print(isimSoyisim.lower())
print(isimSoyisim.upper())
print(isimSoyisim.find("a"))

marka = "Honda"
# print(f"o'nun indisi = {marka.index("t")}")
# print(f"o'nun indisi = {marka.find("t")}")

# immutable -> değiştirilemez
ders = "Python gelistirme"
ders = "C# gelistirme"
print(ders)
ders[2] = "z"
print(ders[2])




