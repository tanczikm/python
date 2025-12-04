ermek = [200, 100, 50, 20, 10, 5]

while True:
    osszeg = input("Kérek egy pozitív összeget, megmondom hogyan lehet felváltani! ")
    if osszeg == "":
        break
    osszeg = int(osszeg)
    
    print(osszeg, "Ft:")

    for i in ermek:
        kivon = (osszeg // i)
        osszeg = (osszeg - (kivon * i))
        
        if i == 5:
            if 5 > osszeg > 2:
                kivon = kivon + 1
                osszeg = osszeg - 5

        if kivon != 0:
            print(kivon, "db", i, "Ft-os")
        

    print("Maradt:", osszeg)

    