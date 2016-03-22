"""
Defineerida funktsioon leidub_yhine(loend1, loend2), mille parameetriteks on kaks
loendit ja mis tagastab tõeväärtuse, mis näitab, kas need loendid omavad vähemalt ühte ühist
elementi.
"""

# Defineerin funktsiooni leidub_yhine
def leidub_yhine(loend1, loend2):
    # Muudab loendi hulgaks, sest Pythonis hulkade võrdlemine on algoritmiliselt
    # kiirem, kui loendite võrdlemine.
    if set() == set(loend1).intersection(loend2):
        # Kui loendite ühisosa on võrdne tühihulgaga on tulemiks False
        return False
    else:
        # Vastasel juhul on tulemiks True
        return True
    

