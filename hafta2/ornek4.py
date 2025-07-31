# listeler mutabledır yani değiştirilebilir.
yaslar = [23, 27, 32, 45]
# yaslar[0] = 37
# append listenin sonuna eleman eklememizi sağlar
# yaslar.append(54)
# pop listenin sonundan eleman silmemizi sağlar
# yaslar.pop()
# sort listeyi sıralamayı sağlar.
# print(yaslar.sort())
# yaslar.clear()
# print(yaslar)
# print(yaslar.index(27))
# yaslar.remove(27)

# tuple -> immutable
yaslar = (11, 22, 11, 34, 11)
print(yaslar[0])
print(yaslar.count(11))
print(yaslar.index(11))
yaslarListesi = list(yaslar)
print(yaslarListesi)


