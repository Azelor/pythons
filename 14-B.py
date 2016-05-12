from tkinter import *
from tkinter.ttk import *

root = Tk()

def askopenfilename():
    fn = filedialog.askopenfilename()
    arv = 0
    filename = open(fn, "r")
    for rida in filename:
        for taht in rida:
            arv += 1
    lbl.config(text="Fail: " + fn + " Tähti: " + str(arv))

btn_askopenfilename = Button(root, text="Loe fail", command=askopenfilename)
btn_askopenfilename.pack()

lbl = Label(root, text="Fail Avamata")
lbl.pack()

root.mainloop()
