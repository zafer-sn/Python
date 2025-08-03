"""
class -> sınıf
object -> instance -> nesne -> obje
"""
yas = 50
class Ogrenci():
    isim = ""
    soyisim = ""
    yas = 0
    kilo = 0.0
    boy = 0.0

berke = Ogrenci() # Ogrenci berke = new Ogrenci();
berke.isim = "Berke"
berke.soyisim = "Deneme"
berke.yas = 23
esra = Ogrenci()
esra.isim = "Esra"
ilayda = Ogrenci()
ilayda.isim = "İlayda"
print(berke.isim)
print(esra.isim)
print(ilayda.isim)
