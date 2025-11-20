szam = int(input("Add meg a piramis magasságát: "))

csillagok = "*"

for i in range(1, szam+1):
    print(csillagok)
    #print(i)
    csillagok = csillagok + "*"