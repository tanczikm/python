# bekér és megállapítjuk: páros vagy páratlan

szam = int(input("Kérlek adj meg egy számot! "))

maradek = szam % 2
if maradek == 1:
    print("A szám páratlan.")
elif maradek == 0:
    print("A szám páros.")