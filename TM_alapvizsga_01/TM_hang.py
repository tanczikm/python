def hangtartomany(frekvencia):
    if frekvencia < 20:
        return "infra"
    elif frekvencia <= 20000:
        return "hallható"
    return "ultra"



while True:
    frekvencia = int(input("Kérem, adjon meg egy frekvenciát: "))
    if frekvencia == 0:
        print("Vége")
        break
    print(f"A(z) {hangtartomany(frekvencia)} tartományba tartozik.")
