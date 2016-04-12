loend = range(1, 10)
# leia esimene kolmega jaguv arv
leitud = False

for arv in loend:
    if arv % 2 == 0:
        leitud = True
        break
print(leitud)
