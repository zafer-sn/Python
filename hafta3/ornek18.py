x = 10
y = 20
x = y
y = 50
print(x)
print(y)

class Ogrenci():
    isim = ""

esra = Ogrenci()
esra.isim = "Esra"
ilayda = Ogrenci()
ilayda.isim = "İlayda"
esra = ilayda # esra.isim = "ilayda"
ilayda.isim = "Ayse"
print(esra.isim)
print(ilayda.isim)



