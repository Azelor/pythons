# Impordi moodul kilpkonnagraafika
import turtle

def joonista_kuusk(tasemeid):
    "Defineeri funktsioon kuuse joonistamiseks"
    # Määran joonistamiseks värvi
    turtle.pencolor("green")
    turtle.fillcolor("green")
    # Määran okstepüramiidi algsuuruse
    suurus = 30
    for a in range(tasemeid):
        # Joonista kolmnurk ja täida see värviga
        turtle.begin_fill()
        turtle.circle(-suurus, steps=3)
        turtle.end_fill()
        # Liigu uude asukohta järgmise kolmnurga jaoks
        turtle.right(90)
        turtle.forward(suurus/2)
        turtle.left(90)
        # Suurenda järgmise kolmnurga suurust
        suurus += suurus/4
        

        
