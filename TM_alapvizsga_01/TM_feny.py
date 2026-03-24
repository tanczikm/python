hullamhossz = int(input("Kérem, adjon meg egy hullámhosszt: "))
szin = ""

if hullamhossz >= 420 and hullamhossz < 440:
    szin = "Indigókék"
elif hullamhossz >= 440 and hullamhossz < 490:
    szin = "Kék"
elif hullamhossz >= 490 and hullamhossz < 570:
    szin = "Zöld"
elif hullamhossz >= 570 and hullamhossz < 585:
    szin = "Sárga"
elif hullamhossz >= 585 and hullamhossz < 620:
    szin = "Narancs"
elif hullamhossz >= 620 and hullamhossz < 780:
    szin = "Vörös"

def szinKiir():
    if szin != "":
        print(f"{szin} színnek látjuk.")
    else:
        print("Nem látható.")

szinKiir()