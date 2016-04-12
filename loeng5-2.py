loend = [1,2,3,4, 55, 6, 33, 66, 1, 2]
suurim = 0
suurim_i = None
for i in range(len(loend)):
    arv = loend[i]
    if arv > suurim:
        suurim = arv
        suurim_i = i #viimase elemendi indeks

        
print(suurim, suurim_i)
