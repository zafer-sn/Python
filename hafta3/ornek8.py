def topla(*args):
    toplam = 0
    for i in args:
        toplam = toplam + i
    return toplam

print(topla(3, 7, 23))