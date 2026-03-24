print("1. feladat")
heti_aktivitas = input("Adja meg az aktivitását: ")

print("2. feladat")

futas = 0
uszas = 0
gyaloglas = 0
kerekparozas = 0


for betu in heti_aktivitas:
    if betu == "F":
        futas = futas + 2
    if betu == "U":
        uszas = uszas + 1
    if betu == "G":
        gyaloglas = gyaloglas + 1
    if betu == "K":
        kerekparozas = kerekparozas + 10

tavolsag = futas + uszas + gyaloglas + kerekparozas
print(f"Az elért távolság: {tavolsag} km.")
print(f"3. feladat")

if futas != 0 and uszas != 0 and gyaloglas != 0 and kerekparozas != 0:
    print("Bravó! Jutalma még 10 km.")
    tavolsag = tavolsag + 10
else:
    print("Nem jár jutalom.")

print("4. feladat")

def uzenetKuld(tav):
    if tav >= 40:
        return "Gratulálok, kihívás teljesítve!"
    return "Legközelebb sikerül!"

print(f"Eredménye: {tavolsag} km. {uzenetKuld(tavolsag)}")