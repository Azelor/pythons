# joonista kõik hulknurkade/värvide kombinatsioonid
# vastavad loendid on antud
import turtle

kyljed = [3,4,5,9]
varvid = ["red", "green", "blue"]

for v in varvid:
    for k in kyljed:
        print(k, v)
        turtle.down()
        turtle.fillcolor(v)
        turtle.begin_fill()
        turtle.circle(10, steps=k)
        turtle.end_fill()
        turtle.up()
        turtle.forward(25)
