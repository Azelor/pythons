import turtle
turtle.speed(0)
turtle.up()
turtle.back(200)
turtle.down()

def koch(pikkus, min_pikkus):
    
    if pikkus > min_pikkus:
        
        koch(pikkus/3, min_pikkus)
        
        turtle.left(60)

        koch(pikkus/3, min_pikkus)
        
        turtle.right(120)

        koch(pikkus/3, min_pikkus)
        
        turtle.left(60)

        koch(pikkus/3, min_pikkus)
         
    else:
        turtle.forward(pikkus)   


koch(300,10)
