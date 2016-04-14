from os import listdir
from os.path import isdir

def failide_arv(kaust):
    summa = 0
    elemendid = listdir(kaust)
    for element in elemendid:
        pikk_nimi = kaust + "\\" + element
        if isdir(pikk_nimi):
            summa = summa + failide_arv(pikk_nimi)
        else:
            summa += 1

    return summa

print(failide_arv("P:/programmeerimine/"))
