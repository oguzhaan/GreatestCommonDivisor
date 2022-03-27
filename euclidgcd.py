


sayi1 = int(input("Bir sayı giriniz: "))
sayi2 = int(input("İkinci sayiyi giriniz: "))

def EuclidGCD(sayi1, sayi2):
    bolum = 0
    bolum = sayi1%sayi2
    sayi1 = sayi2
    sayi2 = bolum

    if(sayi1%sayi2 == 0):
        return sayi2
    else:
        return EuclidGCD(sayi1,sayi2)


print(EuclidGCD(sayi1,sayi2))





