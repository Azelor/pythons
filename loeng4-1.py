import turtle
import random

arv = int(input("sisesta alaml6ikude arv: "))
dis = 10
turtle.pensize(10)
for i in range(arv):
    turtle.circle(dis, extent=30)
    turtle.left(30)
    dis = dis + 10
    turtle.pencolor(random.random(),random.random(),random.random())
