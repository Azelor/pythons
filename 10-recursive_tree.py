import turtle

def joonista_puu(tyve_pikkus, min_haru_pikkus):
    """
    Joonistab puu.
    Puu on fraktaalne/rekursiivne kujund,
    mille tüve küljes on kaks lühema tüvega alampuud:
    puu haru. Kui tyve_pikkus < min_haru_pikkus,
    siis puu koosneb ainult tüvest.
    Funktsioon taastab kilpkonna algse oleku.
    """
    # Joonista tüvi
    turtle.forward(tyve_pikkus)
    # Kui tyve_pikkus > min_haru pikkus
    if tyve_pikkus > min_haru_pikkus:
        # Keera kilpkonna 45 kraadi vasakule
        turtle.left(45)
        # Joonista esimene alampuu 0.6*tyve_pikkus
        joonista_puu(0.7*tyve_pikkus, min_haru_pikkus)
        # Keera kilpkonna 90 kraadi paremale
        turtle.right(90)
        # Joonista teine alampuu
        joonista_puu(0.7*tyve_pikkus, min_haru_pikkus)
        # Taasta algne suund
        turtle.left(45)
    # Taasta algne olek
    turtle.back(tyve_pikkus)

turtle.speed(0)
turtle.left(90)
joonista_puu(100, 10)
