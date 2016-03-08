# Küsi kasutajalt järjest loendi elemente ja lisa neid loendisse.

loend = []
sisend = "alg"
while sisend != "":
    sisend = input("lisa element: ")
    loend.append(sisend)

del loend[-1]
print(loend)

