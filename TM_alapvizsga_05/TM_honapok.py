tavasz = [3, 4, 5]
nyar = [6, 7, 8]
osz = [9, 10, 11]
tel = [12, 1, 2]

def honap(ho):
    if ho in tavasz:
        return "Tavasz"
    if ho in nyar:
        return "Nyár"
    if ho in osz:
        return "Ősz"
    if ho in tel:
        return "Tél"
    return "Nincs ilyen hónap!"

while True:
    ho = input("Adja meg hányadik hónap van:(1-12) ")
    if ho == "":
        break
    print(honap(int(ho)))
    

    