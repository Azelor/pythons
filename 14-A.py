from tkinter import *
from tkinter.ttk import *

root = Tk()

def prindiHello():
    print("Hello World!")

button = Button(root, text="Hello!", command=prindiHello)
button.pack()

root.mainloop()
