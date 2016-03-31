def leidub_yhine(loend1, loend2):
    "Kas loend1 ja loend2 omavad ühist elementi?"
    #Käi läbi loend1 elemendid
    for element in loend1:
        # Kui element sisaldub loend2-s, tagasta True
        if element in loend2: return True
    # Muidu tagasta False
