import turtle
import random


dis = 20
turtle.pensize(10)
for i in range(40):
    turtle.forward(dis)
    turtle.left(90)
    dis = dis + 20
    turtle.pencolor(random.random(),random.random(),random.random())
