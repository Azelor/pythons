import cProfile

# See programm arvutab loendi elementide korrutise

loend = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ,20]
tulem = 1 # algväärtustamine
for element in loend:
    tulem = tulem * element #või muu operatsioon
print("Loendi elementide korrutis", tulem)


cProfile.run('print("Loendi elementide korrutis", tulem)')
