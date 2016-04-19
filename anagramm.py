from itertools import permutations
from doctest import testmod
from collections import Counter
import cProfile # tööaja mõõtmise moodul


def anagramm(s1, s2):
    """
    Tagastab, kas stringid s1 ja s2 on anagrammid.
    Stringid on anagrammid kui ühest saab märke
    ümber paigutades teist teha.

    >>> anagramm("keel", "leek")
    True
    
    >>> anagramm("keel", "meel")
    False
    """
    # Toore jõuga töötav  (brute-force) algoritm
    # Käi läbi s2 märkide kõik võimalikud permutatsioonid p
    for p in permutations(s2):
        # Kui s1 = p, siis tagasta True
        if s1 == "".join(p):
            return True
    # Tagasta False
    return False


def anagramm2(s1, s2):
    """
    Tagastab, kas stringid s1 ja s2 on anagrammid.
    Stringid on anagrammid kui ühest saab märke
    ümber paigutades teist teha.

    >>> anagramm("keel", "leek")
    True
    
    >>> anagramm("keel", "meel")
    False
    """
    # Kaks stringi on anagrammid kui
    # nende märgisagedused on võrdsed
    return Counter(s1) == Counter(s2)    


def anagramm3(s1, s2):
    """
    Tagastab, kas stringid s1 ja s2 on anagrammid.
    Stringid on anagrammid kui ühest saab märke
    ümber paigutades teist teha.

    >>> anagramm("keel", "leek")
    True
    
    >>> anagramm("keel", "meel")
    False
    """
    # Kaks stringi on anagrammid kui
    # nende sorditud märgijadad on võrdsed
    return sorted(s1) == sorted(s2)


testmod() # Testi dok. stringe
print(anagramm3("keel", "leke"))
print(anagramm3("helloworld", "abcdefghij"))
print(anagramm3("helloworld!?", "abcdefghij?!"))
cProfile.run('anagramm("helloworld!?"*100000, "abcdefghij?!"*100000)')
cProfile.run('anagramm2("helloworld!?"*100000, "abcdefghij?!"*100000)')
cProfile.run('anagramm3("helloworld!?"*100000, "abcdefghij?!"*100000)')
