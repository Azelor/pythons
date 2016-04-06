import operator

def sagedused(failinimi):
    sagedus={}
    fail= open(failinimi, 'r')
    tekst = fail.read()
    for symbol in tekst:
        sagedus[symbol]=tekst.count(symbol)
    fail.close()
    sorditud = sorted(sagedus.items(), key=operator.itemgetter(1), reverse=True)
    print(sagedus)
    return sorditud

print(sagedused("kodeeritud_yl.txt"))



    


