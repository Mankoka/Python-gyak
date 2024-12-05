
import random  # Random modul importálása

def veletlen():
    hossz = 20
    lista = []
    for i in range(hossz):
        lista.append(random.randint(1, 50))  # Véletlenszámok generálása
    return lista

def kiir():
    for i in veletlen():  # Végigmegyünk a `veletlen()` által visszaadott listán
        print(i, end=" ")  # Kiírjuk az elemeket

def osszeAd():
    sum = 0
    for i in veletlen():
        sum = sum + i
    return sum

veletlen()
kiir()  # Csak a `kiir()` meghívása szükséges, mert az magában hívja a `veletlen()`-t
print()
print(f"A lista elemeinek összege: {osszeAd()}")

