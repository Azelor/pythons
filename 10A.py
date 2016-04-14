import turtle

def joonista_puu(tyve_pikkus, min_haru_pikkus):
    # Joonista tüvi
    turtle.forward(tyve_pikkus)
    # Kui tyve_pikkus > min_haru pikkus
    if tyve_pikkus > min_haru_pikkus:
        # Keera kilpkonna 45 kraadi vasakule
        turtle.left(45)
        # Joonista esimene alampuu 0.6*tyve_pikkus
        joonista_puu(0.6*tyve_pikkus, min_haru_pikkus)
        # Keera kilpkonna 90 kraadi paremale
        turtle.right(90)
        # Joonista teine alampuu
        joonista_puu(0.6*tyve_pikkus, min_haru_pikkus)
        # Taasta algne suund
        turtle.left(45)
        # Joonista kolmas alampuu (pisut pikem, et ei lõikuks)
        joonista_puu(0.75*tyve_pikkus, min_haru_pikkus)
    # Taasta algne olek
    turtle.back(tyve_pikkus)

turtle.speed(0)
turtle.left(90)
joonista_puu(100, 30)
