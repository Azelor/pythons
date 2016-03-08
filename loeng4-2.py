sisend = int(input("sisestage pos t2isarv: "))

jagatav = sisend

while jagatav > 1:
    assert jagatav > 1
    jagatav = jagatav / 2
    print(jagatav)

if jagatav == 1:
    print(sisend, "oli kahe aste")

else:
    print(sisend, "ei olnud kahe aste")

