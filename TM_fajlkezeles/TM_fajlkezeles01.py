forrasfajl = open("olvass_ansi.txt", encoding="ansi")

for sor in forrasfajl:
    print(sor.strip()) # a .strip() metódus segítségével eltávolítja a soremelés karaktereket
forrasfajl.close()