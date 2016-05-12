riik = "Eesti: blue,black,white"
riigid = riik.split()

print(riigid[0])

splitLine = riik.split(":")
varvid = splitLine[1].strip().split(",")
print(splitLine[0])
print(varvid)

dictionary = {}
dictionary[splitLine].append(varvid)
dictionary
