# 4. Feladat
# Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!


def kiir_legrovidebb(lista):
    legrovidebb = lista[0]
    for i in range(len(lista)):
        if len(lista[i]) < len(legrovidebb):
            legrovidebb = lista[i]

    print("A legrövidebb szó:", legrovidebb)





szavak = []

for i in range(3):
    szavak.append(input("Adj meg egy szót! "))


kiir_legrovidebb(szavak)
