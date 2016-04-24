
def sisaldab(sorditudloend, x):
    """
    Tagastab tõeväärtusena, kas sorditud loend sisaldab elementi x.
    Sorditud loend peab olema sorditud kasvavas järjekorras.
    """
    alumine = 0
    ylemine = len(sorditudloend) - 1
    while alumine <= ylemine:
        keskmine = (alumine + ylemine) // 2
        if sorditudloend[keskmine] == x:
            
            return True
        elif sorditudloend[keskmine] > x:
            
            ylemine = keskmine - 1
        else:
            alumine = keskmine + 1
    return False


l= [1, 2, 3, 4, 7, 90]
print(sisaldab(l, 1))
print(sisaldab(l, 7))
print(sisaldab(l, 90))
print(sisaldab(l, 0))
print(sisaldab(l, 20))
print(sisaldab(l, 200))


    
    
