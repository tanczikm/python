def kiir(szam1, szam2):
    print("-----------------------------")
    print(f"A {szam1} és {szam2} közötti számok:")

    if szam1 > szam2:
        for i in range(szam2+1, szam1):
            print(i)
    else:
        for i in range(szam1+1, szam2):
            print(i)
    print("-----------------------------")

kiir(int(input("Add meg az első számot: ")), int(input("Add meg a második számot: ")))