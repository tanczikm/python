# "S" méret: 53 gramm alatti.
# "M" méret: 53-63 gramm közötti.
# "L" méret: 64-73 gramm közötti.
# "XL" méret: 73 gramm feletti.

tomeg = int(input("Kérem adja meg, hány grammos a tojás: "))

if tomeg < 53:
    kategoria = "S"

elif tomeg >= 53 and tomeg <= 63:
    kategoria = "M"

elif tomeg >= 64 and tomeg <= 73:
    kategoria = "L"

else:
    kategoria = "XL"


print("A tojás kategóriája: \"", kategoria, "\"", sep='')