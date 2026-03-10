ingatlantipusok = ["Családi ház", "Ikerház", "Sorház", "Lakás"]

with open("ingatlantipusok.txt", "w", encoding="utf-8") as celfajl:
    for tipus in ingatlantipusok:
        print(tipus, file=celfajl)