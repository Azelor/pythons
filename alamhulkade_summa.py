def alamhulgad(jada):
    """
    Tagastab jada alamhulkade (loendite) loendi.
    Kasutab rekursiivset algoritmi.
    """
    if len(jada) == 0: # baasjuht
        return [[]]
    pea = jada[0]
    saba = jada[1:]
    tulem = []
    for sabahulk in alamhulgad(saba):
        tulem.append([pea] + sabahulk) # peaga
        tulem.append(sabahulk) # peata
    return tulem


def on_vaike_alamhulk(arvujada, k, t):
    """
    Tagastab, kas arvujada elementidest on võimalik koostada k-elemendiline
    alamhulk, mille summa on väiksem või võrdne kui k.
    """
    for alamhulk in alamhulgad(arvujada):
        if len(alamhulk) == k and sum(alamhulk) <= t:
            return True # Leidsime sobiva
    return False  # Sobivat polnud



testjada = [3, -6, 7]
print("Kõik alamhulgad:", alamhulgad(testjada))
print("[-6] sobib:", on_vaike_alamhulk(testjada, 1, -4))
print("Pole sellist:", on_vaike_alamhulk(testjada, 2, -4))
print("[3, -6, 7] sobib:", on_vaike_alamhulk(testjada, 3, 5))
