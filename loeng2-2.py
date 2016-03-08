#Küsime ainepunktide arvu
ainepunktid = int(input("Sisesta ainepunktide arv:  "))

#kui ainepunktid > 50, siis "Arvestatud"
if ainepunktid <= 100 and ainepunktid >= 0:                
    if ainepunktid > 50 :
        print("Arvestatud!")
    elif ainepunktid <= 50 :
        print("proovi uuesti!")
    else :
        print("test")
else :
    print("Palun sisesta arv 0 ja 100 vahel")

