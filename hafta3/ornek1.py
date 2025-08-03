# break, continue, pass
liste1 = [10, 20, 30, 40, 50, 60]
# print(40 in liste1)
"""
for sayi in liste1:
    print(sayi)
    if sayi == 40:
        print("Listede 40 vardır")
        break
"""
"""
for sayi in liste1:
    print(sayi)
    if sayi == 40:
        print("Listede 40 vardır")
        continue # o anki döngü iterasyonunu bitirip bir sonrakine geçer
"""

for i in range(0, 101):
    if i % 2 == 1:
        continue
    print(i)

for i in range(100):
    pass
print("selam")



