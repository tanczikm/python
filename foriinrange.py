import time

# 0-tól kezdi a számolást
KEZDES = 0

# Meddig számoljon el?
MEDDIG = 10

# A KEZDES-hez minden körben mennyit adjon hozzá
LEPES = 2

# A lényeg:
# Addig fog futni újra és újra, amíg a SZAM értéke kisebb a MEDDIG értékénél.
# KEZDES-től kezdi a számolást, minden körben a LEPES-t hozzáadja a SZAM-hoz.
#                    0       10      2
for SZAM in range (KEZDES, MEDDIG, LEPES):
    print()
    print("SZAM értéke:", SZAM)
    print("KEZDES értéke:", KEZDES)
    print("MEDDIG értéke:", MEDDIG)
    print("LEPES értéke:", LEPES)
    input()