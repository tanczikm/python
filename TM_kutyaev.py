kor = int(input("Add meg a kutya életkorát emberi években! "))

kutyakor = 0

for i in range(kor):
    if i == 0 or i == 1:
        kutyakor = kutyakor + 12
    else:
        kutyakor = kutyakor + 4

print("A kutyád", kutyakor, "éves kutyaévben.")