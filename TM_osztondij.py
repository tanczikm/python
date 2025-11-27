jegyekszama = int(input("Hallgato jegyeinek szama: "))
osszeg = 0

print("A jegyek:")

for i in range(0, jegyekszama):
    osszeg = osszeg + int(input())

atlag = (osszeg / jegyekszama)

print("A jegyek atlaga:", atlag)

if atlag >= 4.0:
    print("A hallgato osztondijra jogosult.")
else:
    print("A hallgato nem jogosult osztondijra.")