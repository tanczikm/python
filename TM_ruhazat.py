hofok = int(input("Hány fok van most? "))

if hofok < 10:
    print("Nagyon hideg van, vegyél kabátot és sapkát!")

elif hofok <= 20:
    print("Hűvös az idő, érdemes pulóvert venni.")

elif hofok > 20:
    print("Meleg van, elég egy póló is.")