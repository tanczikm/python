nev = input("Kérem, adja meg a nevét: ")
szuletes = int(input("Kérem, adja meg a születési évét: "))

if szuletes < 1965 or szuletes > 2012:
    print("Sajnálom, nem beazonosítható év!")

elif szuletes <= 1979:
    print(f"Kedves {nev}, Ön X generációs")

elif szuletes <= 1994:
    print(f"Kedves {nev}, Ön Y generációs")

elif szuletes <= 2012:
    print(f"Kedves {nev}, Ön Z generációs")
