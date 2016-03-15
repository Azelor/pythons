loend = [1,2,3,4,8,9, 11, 13, 14, 18]
paarisarvud = loend[:] # teeb loendist oopia

# eemdalda loendist need arvud, mis pole paarisarvud
for arv in loend:
    if arv % 2 != 0:
        paarisarvud.remove(arv) #probleem: tsükli loendit muudetakse tsükli sees.
print(paarisarvud)
