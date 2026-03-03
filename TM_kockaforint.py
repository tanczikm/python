import random

def NapiOsszeg(napSorszam):
    return dani_dobasai[napSorszam-1]*10
    


dani_dobasai = []
dani_dobasai_string = ""

for nap in range(14):
    dobas = random.randint(1, 6)

    dani_dobasai.append(dobas)

    dani_dobasai_string = dani_dobasai_string + str(dobas) + " " 

print("A dobott számok:")
print(dani_dobasai_string)

nap = int(input("Melyik napra kíváncsi? Adja meg a számát: "))
if nap < 1 and nap > 14:
    print("Hibás nap!")
else:
    print(f"A kérdezett nap: {nap}, ekkor {NapiOsszeg(nap)} Ft került az üvegbe.")


osszesen = 0
nagyobb_mint_ot = 0
for szam in dani_dobasai:
    osszesen = osszesen + szam*10
    if szam >= 5:
        nagyobb_mint_ot = nagyobb_mint_ot + 1
print(f"{osszesen} Ft-ot gyűjtött Dani összesen")
print(f"Dani {nagyobb_mint_ot} napon tett félre legalább 50 Ft-ot.")