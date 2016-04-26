def valiksortimine(loend):
    """Tagastab loendi elementide järjestatud variandi

    See algoritm ei ole mäluefektiivne"""

    # Tee algselt tühi sorditute loend
    sorditud = []

    # Tee loendist koopia
    loendi_koopia = loend[:]

    # Kuni loendis on veel elemente (n korda)
    while len(loendi_koopia) > 0:
        # Leiame loendi minimaalse element (lineaarne keerukus, n)
        minimaalne = min(loendi_koopia)
        # Lisa minimaalne element sorditute hulka (konstantne keerukus)
        sorditud.append(minimaalne)
        # Eemalda minimaalse elemendi loendi koopiast (konstantne keerukus)
        loendi_koopia.remove(minimaalne)
    return sorditud

print(valiksortimine([3, 4, 1, 9, 4, 4]))
    

def kiirsorditud(loend):
    """
    Tagastab loendi elementide järjestatud variandi

    Ajaline keerukus on n log n
    """
    if len(loend) <= 1:
        return loend

    juhtelement = loend[0]

    vaiksemad = []
    vordsed = []
    suuremad = []

    for element in loend:
        if element < juhtelement:
            vaiksemad.append(element)
        elif element == juhtelement:
            vordsed.append(element)
        elif element > juhtelement:
            suuremad.append(element)
    # Sordi rekursiivselt juhtelemendist väiksemad
    vaiksemad = kiirsorditud(vaiksemad)
    # Sordi rekursiivselt juhtelemendist suuremad
    suuremad = kiirsorditud(suuremad)
    # Tagasta väiksemad + võrdsed + suuremad

    return vaiksemad + vordsed + suuremad

print(kiirsorditud([3, 4, 1, 9, 4, 4]))
