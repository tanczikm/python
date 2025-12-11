import math

while True:
    n = int(input("Adj meg egy oldal számot! "))
    a = int(input("Adj meg egy oldal hosszúságot! "))

    if n < 3 or a <= 0:
        print("Az oldalak száma nem lehet kisebb 3-nál és az oldal hosszúsága nem lehet 0 vagy kevesebb.")
        continue

    else:
        terulet = ((n * (a**2)) / (4 * math.tan(math.pi / n)))
        terulet = round(terulet, 2)

        print("A szabályos sokszög területe:", terulet)
        break