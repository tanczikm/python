# Írj egy Python programot, amely bekéri a hőmérsékletet Celsius-fokban, majd az alábbi szabályok szerint ad öltözködési tanácsot: (XYhomerseklet.py)
# 36°C felett → „Nagyon meleg van, vegyél könnyű ruhát és igyál sok vizet!”
# 26-35°C között → „Meleg van, viselj pólót és rövidnadrágot.”
# 16-25°C között → „Kellemes idő van, egy vékony pulóver elég lehet.”
# 6-15°C között → „Hűvös van, öltözz rétegesen és vigyél kabátot!”
# 0-5°C között → „Hideg van, meleg kabát és sapka ajánlott.”
# 0°C alatt → „Nagyon hideg van, öltözz rétegesen és hordj kesztyűt, sapkát!”

homerseklet = int(input("Add meg a hőmérsékletet Celsius-fokban: "))

if homerseklet >= 36:
    print("Nagyon meleg van, vegyél könnyű ruhát és igyál sok vizet!")

if homerseklet >= 26 and homerseklet <= 35:
    print("Meleg van, viselj pólót és rövidnadrágot.")

if homerseklet >= 16 and homerseklet <= 25:
    print("Kellemes idő van, egy vékony pulóver elég lehet.")

if homerseklet >= 6 and homerseklet <= 15:
    print("Hűvös van, öltözz rétegesen és vigyél kabátot!")

if homerseklet >= 0 and homerseklet <= 5:
    print("Hideg van, meleg kabát és sapka ajánlott.")

if homerseklet < 0:
    print("Nagyon hideg van, öltözz rétegesen és hordj kesztyűt, sapkát!")