
def paaritud_arvud(n):
    arvud = ""
    # For loop. 1-st n+1-ni. 2 sammu kaupa. 
    for i in range(1, n+1, 2):
        # Lisab käesoleva arvu stringile lõppu.
        arvud += str(i)
        # Lisab vahele koma, välja arvatud viimasele
        if i < n-1:
            arvud += ", "      
    return arvud
    

def kirjuta_paaritud(n, fn):
    "Kasutab funktsiooni paaritud_arvud parameetriga n ja lisab tulemi faili fn"
    file = open(fn, "w")

    file.write(paaritud_arvud(n))

    file.close()

kirjuta_paaritud(7,"arvud.txt")

