import turtle

def joonista_hulknurk(nurkade_arv, varv, raadius=50):
    """
    Joonistab värvilise hulknurga.
    nurkade_arv = täisarv (> 3)
    varv - turtle mooduli jaoks sobilik värv
    raadius - hulknurga nurga kaugus hulknurga keskpunktist
    """
    # Määra värv, alusta kujundi täitmist
    turtle.fillcolor(varv)
    turtle.begin_fill()
        
    # Joonista hulknurk
    turtle.circle(raadius, steps=nurkade_arv)
    
    # Lõpeta kujundi täitmine värviga
    turtle.end_fill()

joonista_hulknurk(2*3,"yellow", raadius=100)
