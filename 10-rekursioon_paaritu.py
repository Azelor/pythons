def paaritud_arvud(n,algus=1):
    """
    Tagastab paaritud arvud vahemikus algus..n loendina
    algus peab olema paaritu
    n peab olema suurem kui algus
    """
    # Rekursiooni baasjuht (algus > n): tagasta tühi loend
    if algus > n:
        return []
    else:
    # Üldjuhul tagastsa algus ja paaritud arvud algus+2-st n-ni
        return [algus] + paaritud_arvud(n, algus=algus+2)

x = paaritud_arvud(10, algus=2)
print(x)

def paaris_arvud(n,algus=1):
    """
    Tagastab paaritud arvud vahemikus algus..n loendina
    algus peab olema paaritu
    n peab olema suurem kui algus
    """
    # Rekursiooni baasjuht (algus > n): tagasta tühi loend
    if algus > n:
        return []
    else:
    # Üldjuhul tagastsa algus ja paaritud arvud algus+2-st n-ni
        return [algus] + paaritud_arvud(n, algus=algus+2)

x = paaritud_arvud(10)
print(x)
