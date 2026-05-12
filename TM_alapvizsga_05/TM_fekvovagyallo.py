szelesseg = int(input("Adja meg a téglalap szélességét! "))
magassag = int(input("Adja meg a téglalap magasságát! "))

if magassag > szelesseg:
    print(f"Ez egy álló téglalap. Területe: {szelesseg * magassag}")

if szelesseg > magassag:
    print(f"Ez egy fekvő téglalap. Területe: {szelesseg * magassag}")

else:
    print(f"A téglalap egy négyzet. Területe: {szelesseg * magassag}")