liste = ["Zafer", "Zafer SERİN", "Ahmet", "Ahmet YILMAZ"]

def bul(metinsel):
    return "Zafer" in metinsel

print(list(filter(bul, liste)))