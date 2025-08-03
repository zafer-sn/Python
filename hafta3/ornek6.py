# fonksiyonlar - metotlar
"""
1- parametre almayan ve değer döndürmeyen fonksiyon
2- parametre alan ve değer döndürmeyen fonksiyon
3- parametre almayan ve değer döndüren fonksiyon
4- parametre alan ve değer döndüren fonksiyon
"""
# def -> define
def selamla():
    print("Hoşgeldiniz..")

selamla()
selamla()
selamla()
selamla()

def topla(sayi1, sayi2):
    print(sayi1 + sayi2)

topla(11, 22)
topla(-54, 25)
topla(23, 7)

def hesapla(sayi1):    
    return sayi1 * 2 - 3

print(hesapla(5) * 2)


# f(x, y) = (x^3 + y ^ 2 + 5)/3
# f (2, 3) = (8 + 9 + 5)/3 -> 7...

def fonksiyonHesapla(x, y):
    return (x ** 3 + y ** 2 + 5) / 3
print(fonksiyonHesapla(2, 3))
print(fonksiyonHesapla(5, 7))

# Asal sayı örneği
# 11, 5, 8, 17, 21
# en kucuk asal sayi 2'dir
# -se -sa -> şart demektir -> if
def asalmi(sayi):
    gelenSayiAsalmi = True
    for i in range(2, sayi):
        if sayi % i == 0:
            gelenSayiAsalmi = False
            break
    return gelenSayiAsalmi
while True:
    sayi = int(input("Lütfen asal olup olmadığını kontrol etmek istediğiniz sayiyi giriniz..:"))
    if sayi == 0:
        break
    if asalmi(sayi):
        print("Girilen sayi asaldir")
    else:
        print("Girilen sayi asal değildir!")





