# 4. Feladat
# Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

# A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!

def kerulet(arg0, *args):
    parameterekSzama = 0
    for arg in args:
        parameterekSzama = parameterekSzama + 1
    
    if parameterekSzama == 0:
        return "négyzet"
    if parameterekSzama == 1:
        return "téglalap"
    if parameterekSzama == 2:
        return "háromszög"
    return "sokszög"

print(kerulet("kotelezo"))
print(kerulet("kotelezo", 1))
print(kerulet("kotelezo", 1, 2))
print(kerulet("kotelezo", 1, 2, 3))
print(kerulet("kotelezo", 1, 2, 3, 4))