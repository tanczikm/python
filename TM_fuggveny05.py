# 5. Feladat
# Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír! A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely a lista legkisebb elemével tér vissza. A program írja ki, hogy melyik volt a megadott legkisebb szám!

def listaLegkisebb(lista):
    legkisebb = lista[0]

    for szam in lista:
        if szam < legkisebb:
            legkisebb = szam
    
    return legkisebb


lista = []

while True:
    szam = int(input("Adj meg egy számot! "))
    if szam < 0:
        print(lista)
        print("Legkisebb:", listaLegkisebb(lista))
        break

    lista.append(szam)