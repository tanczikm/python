# 3.1 Feladat
# Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!

def harommal_oszthatok(lista):
    eredmeny = 0
    for szam in lista:
        if szam % 3 == 0:
            eredmeny = eredmeny + 1
    
    return eredmeny

# print(harommal_oszthatok([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 3.2 Feladat
# Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)

lista = []

while True:
    szam = int(input("Adj meg egy számot (negatív szám: kilépés): "))
    if szam < 0:
        print(lista)
        print(harommal_oszthatok(lista))
        break
    lista.append(szam)
    