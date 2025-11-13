count = 0

while True: # végtelen ciklust indít
    count += 1

    if count > 5: # megállási feltétel
        break
    
    if count == 3: # a 3-as értéket átugorjuk
        continue

    print(count, "Éljen a Python!")
