import turtle
while True:
#Küsime kasutajalt hulknurga külgede arvu
    try:
        nurkadeArv = int(input("Mitme nurgaga hulknurka tahad?  "))
        if nurkadeArv <= 2:
            print("Liiga väike arv")
        else:
            turtle.circle(100, steps=nurkadeArv)
    except:
        print("Palun sisesta arv!")

#Joonistame hulknurga        


