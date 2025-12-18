jegyszam = int(input("Hány buszjegyet szeretnél venni? "))

fizetendo = 450 * jegyszam

print(f"Fizetendő összeg: {fizetendo} Ft")

if fizetendo > 3000:
    kedvezmeny = input("Kérsz kedvezményt? (igen/nem) ")
    if kedvezmeny == "igen":
        fizetendo = fizetendo * 90 / 100
        print(f"Fizetendő összeg: {int(fizetendo)} Ft")
    else:
        print("Köszönjük a vásárlást!")


else:
    print("Köszönjük a vásárlást!")