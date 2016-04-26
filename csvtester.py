import timeit
from sortimine import valiksorditud, kiirsorditud
from random import shuffle

def kirjuta_csv(veerg_n, veerg_t, failinimi, eesti=True):
    """
    veerg_n, veerg_t on veergudele vastavad loendid
    failinimi on .csv faili nimi, kuhu need kirjutada (.csv laiend lisatakse)
    .csv faili formaat (mitte-inglise komad arvudes ','):
    veerg1 päis; veerg2 päis
    v11; v12
    v21; v22
    ...
    vm1; vm2
    Eeltingimuseks on veerg_t ja veerg_n võrdne pikkus
    """
    assert len(veerg_n) == len(veerg_t)
    
    # Ava fail
    csvfail = open(failinimi + ".csv", "w")

    # Kirjuta päis
    if eesti:
        eraldaja = ";"
    else:
        eraldaja = ","
        
    csvfail.write("n" + eraldaja + "t \n")
    
    # Kirjuta read
    for i in range(len(veerg_n)):
        n = veerg_n[i]
        t = veerg_t[i]
        rea_str = str(n) + eraldaja + str(t) + "\n"
        if eesti:
            rea_str = rea_str.replace(".", ",")
        csvfail.write(rea_str)

    # Sulge fail
    csvfail.close()


def fO1(n):
    # Konstantne keerukus
    return (n + 100)**200

def fOn(n):
    # Lineaarne keerukus
    tulem = 0
    for i in range(n):
        tulem += 1
    return tulem

def fOn2(n):
    # Ruutkeerukus
    fOn(n) # Võrdse või nõrgema keerukusega eelnev samm ei mõjuta algoritmi kogukeerukust
    tulem = 0
    for i in range(n):
        for j in range(n):
            tulem += i*j
    return tulem


if __name__ == "__main__":
    testitav_fn = kiirsorditud
    veerg_n = []
    veerg_t = []
    for ni in range(0, 2000, 100):
        segatud = list(range(ni))
        #shuffle(segatud)
        ti = timeit.timeit("testitav_fn(segatud)",
                          setup="from __main__ import testitav_fn, segatud",
                          number=10)
        veerg_n.append(ni)
        veerg_t.append(ti)
    kirjuta_csv(veerg_n, veerg_t, "testKiirsort")
