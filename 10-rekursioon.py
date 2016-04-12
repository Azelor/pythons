""" Näide.
Rekursiooni baas: N: 1 on naturaalarv
Rekursiooni samm: Kui n on naturaalarv, siis n+1 on naturaalarv.

"""

def loenda(n):
    """
    Trükib välja arvud n-st kuni nullini.
    n on positiivne täisarv
    """
    # Rekursiooni baasjuht: (n on null), trüki n
    if n == 0:
        print(n)
    # Rekursiooni üldjuht: (n > 0): trüki n ja loenda (n-1)
    else:
        print(n)
        loenda(n-1) # Rekursiivne väljakutse, läheneb baasjuhule.
    
    

loenda(5)
