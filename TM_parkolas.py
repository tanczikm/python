parkolas = int(input("Adja meg a parkolás időtartamát percben: "))

if parkolas <= 30:
    print("A parkolás ingyenes.")

else:
    if parkolas > 180:
        fizetendo = ((parkolas//60+1)*500*0.9)
    else:
        fizetendo = ((parkolas//60+1)*500)
    print("A fizetendő összeg: ", fizetendo, "Ft.")