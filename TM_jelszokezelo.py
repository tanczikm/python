# bekér egy jelszót: ellenőrzi
#   min 8 karakter
#   kis betű
#   szám

kisbetu = False

while True:
    hossz = 0
    jelszo = input("Kérlek adj meg egy jelszót: ")
    if jelszo == "":
        break

    for i in jelszo:
        hossz = hossz + 1

        if kisbetu != True:
            kisbetu = i.islower()
        


    if hossz < 8:
        print("A jelszónak minimum 8 karakter hosszúnak kell lennie.")
        continue

    if kisbetu != True:
        print("A jelszónak tartalmaznia kell kis betűt.")
        continue



    