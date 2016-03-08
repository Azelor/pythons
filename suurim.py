# See programm peaks väljastama, kas sisestatud arv on algarv

# Sisesta arv!
while True:
    try:
        arv = int(input("Sisestage arv: "))
    except ValueError:
        print("Pole arv")
    else:
        break

# Kontrolli algarvulisust
# Käi läbi kõik võimalikud jagajad
for jagaja in range(2, arv):
    # Kui arv jagub jagajaga, siis leidsime algarvu
    #print(jagaja)
    if (arv % jagaja) == 0:
        print(arv, "Pole algarv!")
        break
else:
        print(arv, "On algarv")

    


    
