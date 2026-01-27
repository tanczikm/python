# 2. Feladat
# Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!


def dontes(szam):
    if szam == 0:
        print("A szám nulla.")
    elif szam < 0:
        print("A szám negatív.")
    else:
        print("A szám pozitív.")

dontes(int(input("Adj meg egy számot! ")))