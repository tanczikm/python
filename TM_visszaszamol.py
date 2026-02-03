def visszaszamol(szam):
    print("Visszaszámlálás indul...")
    if szam < 0:
        for i in range(szam, 1):
            print(i)

    else:
        for i in range(szam, -1, -1):
            print(i)


visszaszamol(int(input("Adj meg egy számot! ")))