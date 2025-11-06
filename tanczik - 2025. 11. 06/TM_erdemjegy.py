# Írj egy Python programot, amely bekér egy pontszámot (0 és 100 között), majd ennek alapján kiírja az érdemjegyet az alábbi szabályok szerint: (XYerdemjegy.py)
# 90-100 pont → Jeles (5)
# 80-89 pont → Jó (4)
# 70-79 pont → Közepes (3)
# 60-69 pont → Elégséges (2)
# 0-59 pont → Elégtelen (1)
# Ha a megadott pontszám nincs 0 és 100 között, a program írja ki, hogy „Érvénytelen pontszám!”.

pont = int(input("Add meg a pontszámot (0-100 között): "))

if pont >= 90 and pont <= 100:
    print("Az osztályzat: Jeles (5)")

elif pont >= 80 and pont <= 89:
    print("Az osztályzat: Jó (4)")

elif pont >= 70 and pont <= 79:
    print("Az osztályzat: Közepes (3)")

elif pont >= 60 and pont <= 69:
    print("Az osztályzat: Elégséges (2)")

elif pont >= 0 and pont <= 59:
    print("Az osztályzat: Elégtelen (1)")

else:
    print("Érvénytelen pontszám!")