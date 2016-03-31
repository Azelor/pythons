import turtle
def trikoloor(riik):
    standardlipud = {'Eesti': ('blue', 'black', 'white'),
 'Leedu': ('yellow', 'green', 'red'),
 'Holland': ('red', 'white', 'blue'),
 'Venemaa': ('white', 'blue', 'red'),
 'Saksamaa': ('black', 'red', 'yellow')}
    varvid = standardlipud[riik]
    counter = 0
    for i in varvid:
        turtle.fillcolor(varvid[counter])
        turtle.begin_fill()
        turtle.forward(90)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(90)
        turtle.right(90)
        turtle.forward(20)
        turtle.end_fill()
        turtle.back(20)
        turtle.right(90)
        counter += 1
        
