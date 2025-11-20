print("Háromszög-e vagy sem? Adj meg három számot!")
# a = int(input("Első szám: "))
# b = int(input("Második szám: "))
# c = int(input("Harmadik szám: "))

while True:
    a = int(input("Első szám: "))
    b = int(input("Második szám: "))
    c = int(input("Harmadik szám: "))

    if (a + b) > c:
        if (a + c) > b:
            if (b + c) > a:
                print("Háromszög.")
                break
    print("Nem háromszög.")
    print("")
    print("Adj meg új számokat:")
