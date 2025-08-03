# prosedürel programlamanın son konusu
# scope(faaliyet alanı) kavramı
x = 10
def yaz(sayi):
    x = 20
    return x * 5
print(yaz(5))
print(x)
