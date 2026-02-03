# Írj eljárást "nagyobbTripla" néven, amely a felhasználótól bekér két számot, majd visszaadja a nagyobb háromszorosát.

def eredmeny(szam1, szam2):
    if szam1 > szam2:
        valasz = szam1*3
    else:
        valasz = szam2*3
    print("A nagyobb szám háromszorosa:", valasz)

eredmeny(int(input("Add meg az első számot: ")), int(input("Add meg a második számot: ")))