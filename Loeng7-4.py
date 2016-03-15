def sonade_sagedused(tekst):
    """
    Tagastsab teksti sõnade (tühiku või muu eraldaja järgi)
    sageduste sõnastiku. Näiteks:
    >>> sonade_sagedused('hei hoo hei hoo')
    >>> {'hei': 2, 'hoo': 2}
    """
    tulem = {} # teeme tühja sõnastiku
    sonade_loend = tekst.split() # teeme sõnade loendi
    print(sonade_loend)
    # Iga sõna jaoks
    for sona in sonade_loend:
        # Suurenda sõna sagedust ühe võrra
        tulem[sona] = tulem.get(sona, 0)+ 1
    #Tagasta tulem
    return tulem

print(sonade_sagedused('hei hoo hei hoo hoo hoo cake pie cake cake cake'))
