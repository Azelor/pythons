from tkinter import *
from tkinter.ttk import *
import turtle

lipud = {}
jarjekord = []

turtle.penup()
turtle.speed(0)
turtle.setx(-400)

def loelipud():
    fn = filedialog.askopenfilename()
    with open(fn) as f:
        for line in f:
            splitLine = line.split(":")
            colors = splitLine[1].strip().split(",")
            lipud[splitLine[0]] = colors
            jarjekord.append(splitLine[0])
    for riik in jarjekord:
        joonistaLipp(riik)

def joonistaLipp(riik, lipud=lipud):
    värvid = lipud[riik]
    turtle.pendown()
    for värv in värvid:
        turtle.begin_fill()
        turtle.fillcolor(värv)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.end_fill()
        turtle.sety(turtle.ycor()-20)
        turtle.right(90)
    turtle.penup()
    turtle.sety(turtle.ycor()+60)
    turtle.setx(turtle.xcor()+110)
    

root = Tk()
c = Canvas(root)
c.config(bg="white")

btn_lipud =  Button(root, text="Loe lipud", command=loelipud)
btn_lipud.pack()

root.mainloop()
