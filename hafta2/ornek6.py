# sözlükler - dictionaries, map
# meyveler = ["elma", "armut", "ayva"]
# kaloriler = [100, 150, 200]
# print(f"{meyveler[0]}'ın kalorisi = {kaloriler[0]}")
# sözlükler key-value -> anahtar-değer ikilisi ile tanımlanır
# keyler -> elma, armut, ayva
# values -> 100, 150, 200
# json -> javascript object notation
# API -> application programming interface -> uygulama geliştirme arayüzü

sozluk1 = {"elma":100, "armut":150, "ayva":200}
print(sozluk1["ayva"])

sozluk2 = {"isim":"Zafer", "verilen_dersler":["Mobil", "Paralel Programlama", "Masaüstü"]}
print(sozluk2["verilen_dersler"][1])

sozluk3 = {100:200, 500:True, "Pi_sayisi":3.14}
print(sozluk3[100])
# print(sozluk3[200])

sozluk4 = {"isim":"Ahmet", "sozluk5": {"Tr":"Türkçe", "En": "İngilizce", "Notlar": [55, 100, 75, 67]}}
print(sozluk4["sozluk5"]["Notlar"][1])

liste2 = ["Zafer", 100, 5.43, False, [1, 2, 3], (3, 5)]

sozluk6 = {"book":"kitap", "flower":"cicek"}
print(sozluk6.keys())
print(sozluk6.values())
print(sozluk6.items())

dict_liste = list(sozluk6.keys())
print(dict_liste[0])

bos_liste = []
print(type(bos_liste))
bos_tuple = ()
print(type(bos_tuple))
bos_set = {}
print(type(bos_set))
bos_sozluk = {}
print(type(bos_sozluk))

bos_set_1 = set()
print(type(bos_set_1))
bos_set_1.add(11)
print(bos_set_1)

bos_liste_1 = list()
bos_tuple_1 = tuple()
bos_sozluk_1 = dict()

# API = "https://api/gpt?bugün_bilecik_hava_durumu"
# "response": "Merhaba, bugün bilecikte hava durumu 10 derecedir."









