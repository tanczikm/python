# Magyarországon a férfiak átlagmagassága 176 cm, a nőké 164 cm. Kérje be a felhasználótól a nemét és a magasságát, majd írja ki, hogy a magassága átlag alatti, átlagos vagy átlag feletti. (Figyelem, kétlépcsős döntésre van szükség!) (XYmagassag.py)

nem = input("Kérem, adja meg a nemét [f/n]: ")
magassag = int(input("Kérem, adja meg a magasságát (egész) centiméterben: "))

if nem == "f":
    if magassag == 176:
        print("Átlagos")
    elif magassag < 176:
        print("Átlag alatti")
    elif magassag > 176:
        print("Átlag feletti")

elif nem == "n":
    if magassag == 164:
        print("Átlagos")
    elif magassag < 164:
        print ("Átlag alatti")
    elif magassag > 164:
        print("Átlag feletti")