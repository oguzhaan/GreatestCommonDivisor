


sayi1 = int(input("İlk sayiyi giriniz: "))
sayi2 = int(input("İkinci sayiyi giriniz: "))

def GreaComDiv(sayi1, sayi2):
    ebob = 0
    for deger in range(1,sayi1+sayi2):
        if (sayi1%deger==0) and (sayi2%deger==0):
            ebob = deger
    return ebob



print(GreaComDiv(sayi1,sayi2))

