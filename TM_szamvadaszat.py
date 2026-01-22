import random

elem_N = int(input("Hány elemű legyen a lista? "))

lista = []

for i in range(elem_N):
    lista.append(random.randint(1, 20))

print(lista)

print(f"A lista első eleme: {lista[0]} utolsó eleme: {lista[elem_N - 1]}")

max_lista = lista[0]
min_lista = lista[0]

for szam in lista:
    if szam > max_lista:
        max_lista = szam
    if szam < min_lista:
        min_lista = szam
    

print(f"Legnagyobb szám: {max_lista} legkisebb szám: {min_lista}")

tiznel_nagyobb = 0
for szam in lista:
    if szam > 10:
        tiznel_nagyobb = tiznel_nagyobb + 1

print(f"10-nél nagyobb számok: {tiznel_nagyobb} darab")

lista.sort()

elso = True
for szam in lista:
    if elso == True:
        elso = False
        szamok_string = szam
        continue

    szamok_string = f"{szamok_string}, {szam}"
    
print(szamok_string)