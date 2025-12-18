szo = input("Kérem, adj meg egy szót! ")

for i in range(len(szo)):
    print(szo[0:i+1])

for i in range(len(szo)):
    i = -1 - i 
    print(szo[0:i])
