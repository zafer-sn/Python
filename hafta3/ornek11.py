# lambda kullanımı
def topla(x, y):
    return x + y

# lambda fonksiyonu karşılığı
topla2 = lambda x,y: x + y

# arrow function ->
print(topla(3, 5))
print(topla2(10, 15))

liste = [10, 20, 30]
print(list(map(lambda x: x/3, liste)))

topla3 = lambda: print("selam")
topla3()
