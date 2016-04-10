""" PAARITUD ARVUD A  --  kirjuta_paaritud_a(n, fn)
Kirjutab soovitud faili paaritud arvud ühest kuni arvuni n.

parameetriks n on täisarv.
parameetriks fn on soovitava tekstifaili nimi(jutumärkide sees). Näiteks "arvud.txt"
"""
def paaritud_arvud_a(n):
    "Kirjutab paaritud arvud ühest n-ni"
    arv = 1
    arvud = []
    # Lisab iga arvu 1-st n-ni loendisse
    while arv <= n:
        arvud.append(arv)
        arv += 2
    # Teeb loendi elementidest stringi
    arvu_string = (', '.join(str(x) for x in arvud))
    return arvu_string
    

def kirjuta_paaritud_a(n, fn):
    "Kasutab funktsiooni paaritud_arvud parameetriga n ja lisab tulemi faili fn"
    file = open(fn, "w")

    file.write(paaritud_arvud_a(n))

    file.close()


""" PAARITUD ARVUD B  --  kirjuta_paaritud_b(n, fn)
Kirjutab soovitud faili paaritud arvud ühest kuni arvuni n.

parameetriks n on täisarv.
parameetriks fn on soovitava tekstifaili nimi(jutumärkide sees). Näiteks "arvud.txt"
"""
def paaritud_arvud_b(n):
    arvud = ""
    # For loop. 1-st n+1-ni. 2 sammu kaupa. 
    for i in range(1, n+1, 2):
        # Lisab käesoleva arvu stringile lõppu.
        arvud += str(i)
        # Lisab vahele koma, välja arvatud viimasele
        if i < n-1:
            arvud += ", "      
    return arvud
    

def kirjuta_paaritud_b(n, fn):
    "Kasutab funktsiooni paaritud_arvud parameetriga n ja lisab tulemi faili fn"
    file = open(fn, "w")

    file.write(paaritud_arvud_b(n))

    file.close()

kirjuta_paaritud_a(7,"arvud1.txt")
kirjuta_paaritud_b(7,"arvud.txt")
