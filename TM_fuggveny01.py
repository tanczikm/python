# 1. Feladat
# Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!

def osszegzo(lista):
    eredmeny = 0
    for szam in lista:
        eredmeny = eredmeny + szam
    return eredmeny

print(osszegzo([1, 2, 3, 4]))