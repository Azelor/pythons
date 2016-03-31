def linnaga_aadressid(aadressid, otsitav_linn):
    "Tagastab aadressid, mis asuvad otsitavas linnas"
    # Tee tühi tulemi loend
    tulem = []
    # Käi aadressid läbi
    for a in aadressid:
        #Leia aadressist linn
        linn = a.split(",")[-1].strip()
        # Kui aadress asub linnas, lisa see tulemisse
        if linn == otsitav_linn: tulem.append(a)
    # Tagasta tulem
    return tulem

aadressid = ["Mustika 15-6, 23456, Mustvee",
 "Oja 12-34, 23456, Mustvee",
 "Jaama 34-56, 12345, Keila",
 "Tartu mnt. 67-89, 12456, Tallinn"]

print(linnaga_aadressid(aadressid, "Mustvee"))
