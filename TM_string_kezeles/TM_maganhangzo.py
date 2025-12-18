mondat = input("Kérlek, adj meg egy mondatot! ")

maganhangzok = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ö", "ő", "ú", "ü", "ű"]

for i in range(len(maganhangzok)):
    betuszam = 0

    for betu in range(len(mondat)):
        if mondat[betu].lower() == maganhangzok[i]:
            
            betuszam = betuszam + 1

    if betuszam != 0:
        print(maganhangzok[i], "betű:", betuszam, "db")

