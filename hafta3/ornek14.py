"""
LEGB
L -> Local -> Yerel
E -> Enclosing -> kapsüllenmiş alan
G -> Global -> Global alan
B -> Built in -> Python fonksiyonlarında böyle bir tanımlama var mı?
"""
isim = "Zafer 1"
def fonksiyon1():
    isim = "Zafer 2"
    def fonksiyon2():
        isim = "Zafer 3"
        print(isim)
    fonksiyon2()
fonksiyon1()
print(isim)
