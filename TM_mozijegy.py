kor = int(input("Hány éves vagy? "))

if kor < 6:
    print("A jegy ingyenes.")

elif kor <= 18:
    print("Diákjegy ára: 1500Ft")

elif kor > 65:
    print("Nyugdíjas jegy ára: 1200Ft")

else:
    print("Teljesárú jegy: 2500Ft")