# t2isarvud on muutmatud objektid
i1 = 10
i2 = i1
i1 = i1 + 9 # i1 saab uue v22rtuse, 19 on eerinev objekt kui 10, i1 viitab.
# mis on i2 v22rtus
print(i2)

i1 = [1,2,3]
i2 = i1

i1.append(4) """kuna list on objekt, siis nii i1 kui ka i2 viitavad temale ja nende väärtused muutuvad kui lisada i1-le juurde element """
print(i2) 

i1 = i1 + [5] #peaks uue listi tekitama
print(i2)
