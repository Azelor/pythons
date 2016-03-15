""" Pythoni andmestruktuurid
Ennik ehk tuple (1, 2, 3)
Hulk ehk set {1, 2, 3}
Sõnastik ehk dictionary [1, "abc" , True]
"""

#Ennik on muutmatmu objekt erinevalt loendist
e = (1, 2, 3)
print(e[0])
print(e + e[1:]) # e + e elemendid alates 1-st.
# e.append(2) annab erinevalt loendist veateate

x = 7
y = 5
e_xy = x, y #selline omistamine annab muutujaks enniku
print(e_xy)
a, b = e_xy #selline omistamine pakib enniku lahti
print(a, b)

# Hulk on matemaatiline hulk (väärtus hulgas võib esineda 1 korra)
# Hulkade vahel on defineeritud ühendi (|), ühisosa (&) ja vahe (-) tehted
# Hulk on muudetav objekt. Hulgal puuduvad indeksid.

hulk1 = {2, 3}
hulk2 = {1, 2, 3}
print("hulkade ühisosa", hulk1 & hulk2)
print("hulkade ühend", hulk1 | hulk2)
print("hulkade vahe", hulk1 - hulk2)
print("Hulgas sisaldumine", 1 in hulk1)
print("Ülemhulgaks olemise kontroll", hulk1 > hulk2)
print("Alam olemise kontroll", hulk1 < hulk2)

#Sõnastik on andmestruktuur, kus indeksi asemel on elementidel
# kasutaja määratud võtmed. Sõnastik on muudetav
# Võti võib olla täisarv, string, ennik.
# Loend ei tohi olla võti.
key1 = "a"
value1 = 1.234
key2 = "b"
value2 = 1.234
d = {key1: value1, key2: value2}
print(d)
print("Element võtme järgi a: ", d["a"])
print("Elemendi küsimine vaikeväärtusega", d.get('a', 0) )
d['c'] = 5.67 # uue elemendi lisamine
d['a'] = 2 # olemasoleva elemeni muutmine
print(d)
for key in d: #iteratsioon käib üle sõnastiku võtmete
    print("võti ja vastav väärtus", key, d[key])

del d['b'] # Elemendi kustutamine.
print("element b on kustutatud\n", d)


