def bol(sayi):
    return sayi / 2

liste = [10, 18, 26, 38, 54]
bosListe = []
print("Dongu basladi")
for sayi in liste:
    bosListe.append(bol(sayi))
print("Dongu bitti")
print(bosListe)

print(list(map(bol, liste)))