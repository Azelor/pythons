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
    

