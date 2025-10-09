pizza = input("Milyen méretű pizzát szeretnél? (kicsi/közepes/nagy): ")

if pizza == "kicsi":
    print("A kicsi pizza ára 2000 Ft.")

elif pizza == "közepes":
    print("A közepes pizza ára 3000 Ft.")

elif pizza == "nagy":
    print("A nagy pizza ára: 4000 Ft.")

else:
    print("Érvénytelen választás. Kérlek kicsi, közepes vagy nagy pizzát válassz!")