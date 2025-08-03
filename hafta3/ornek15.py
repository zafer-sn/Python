x = 30
def fonksiyon1():
    global x
    x = 10

def fonksiyon2():
    global x
    x = 20

fonksiyon1()
fonksiyon2()
print(x)