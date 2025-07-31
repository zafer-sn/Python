# Koşul blokları - if-else
# switch-case - Python'da switch-case yoktur
# >, <, >=, <=, ==, !=
# assign(atamak) operator(=)
girisYapildimi = True
print(5 > 3)
print(2 > 11)
print(5 >= 5)
print(7 == 8)
print(3 != 5)
print(7 != 7)

# and, or ->&&, ||
print(3 > 5 and 7 > 1) # False and True -> False
print(3 > 5 or 7 > 1) # False or True -> True
print(True and True)
"""
and
0 -> False
1 -> True
0 0 0
0 1 0
1 0 0
1 1 1

or
0 0 0
0 1 1
1 0 1
1 1 1
"""

"""
Diğer programlama dilleri
if(3 >5)
{
    Yapılacak işlemler
}
"""

if False:
    print("Selam")
print("Deneme")

# yas = int(input("Lütfen yaşınızı giriniz..:"))
"""if yas >= 18:
    print("Ehliyet alabilirsin")
else:
    print("Ehliyet alamazsın!")"""

"""notOrtalama = float(input("Lütfen not ortalamanızı giriniz..:"))
if notOrtalama > 90.2:
    print("Harf notunuz AA")
elif notOrtalama > 80.5 and notOrtalama <= 90.2:
    print("Harf notunuz AB")
elif notOrtalama >= 70.7 and notOrtalama <= 80.5:
    print("Harf notunuz BA")
else:
    print("Harf notunuz FF")"""


sicaklik = 50.3
nem = 70.3

if sicaklik > 50.0:
    print("Hava çok sıcak")
    if nem > 75.3:
        print("Nem çok düşük")















