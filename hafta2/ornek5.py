# set -> küme -> temelde matematiksel kümelerdir.
# unordered -> sıralanmamış
# unique(nadir,ender) elemanlara sahip olması
liste = [10, 20, 30, 40, 10, 10, 50]
# print(*liste)
print(liste)
set1 = set(liste)
print(set1)
set2 = {20, 50, 10, 110, 110, 55, 250, 50}
print(set2)
# print(set2[0])
set3 = {10, 20, 30, 40, 50}
set4 = {30, 40, 50, 60, 70}
# union -> birlik -> birleşim
print(set3.union(set4))
# intersection -> kesişim
set3.intersection_update(set4)
print(set3)
print(set4)