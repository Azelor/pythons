#küsida kasutajalt arvu, kuni ta allub

while True:
    try:
        arv = int(input("Arv palun: "))
    except ValueError:
        print("No see ei ole arv ju. anna arv!")
    else:
        break
print("Aitäh! Sinu sisestatud arv on: ", arv)
