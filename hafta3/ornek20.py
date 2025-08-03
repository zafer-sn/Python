# class içerisinde tanımlanabilen fonksiyonlara metot adını veriyoruz
def topla():
    return 5
topla()
class Ogrenci():
    isim = ""
    soyisim = ""
    kilo = 0.0
    boy = 0.0
    yas = 0

    # Yapıcı(kurucu) metot
    # init -> initalize -> başlatmak
    # Bir classtan nesne türetildiği anda yapıcı metot çalışır.
    def __init__(self):
        print("selam")

berke = Ogrenci()