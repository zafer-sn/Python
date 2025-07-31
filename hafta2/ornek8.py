# Döngüler(loops)
# for - while
# print(range(100)) # 0 ile 100 arasında 1 er 1 er artan bir yapı oluşturur
# for i in range(10, 100, 5):
#    print(i)

#for i in range(250, 100, -2):
#    print(i)

liste = [3, 11, 24, 51, 23, 11, 24, 55, -24, 43]
liste.append(101)
liste.append(5)
liste.append(10)
liste.append(-3)
print(liste)
# 12 + 1 -> 13
for i in range(0, len(liste)): # i -> 0, 1, 2, ..., 9
    print(liste[i]*2-5)


for j in range(1, 10, 2):
    print(j)
print("------------------------------------------------")
# for-each yapısı
liste2 = [-2, 3, 7]
for eleman in liste2:
    print(eleman)

print("------------------------------------------------")
# unpacking - pytorch - dataloader
liste3 = [(1,2), (3,4), (5,7)]
for (eleman1,eleman2) in liste3:
    print(eleman1)
    print(eleman2)







