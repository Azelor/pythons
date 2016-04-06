file = open('test.txt', 'r')

text = file.read()

print(text)

file.close()


# Teeb hulga kõikidest esinevatest sümbolitest.
symbolid = set()
for symbol in text:
    symbolid.add(symbol)

# Teeb hulgast loendi
loend = list(symbolid)
print(loend)

# loop symbols
tulem = {}
for a in loend:
    tulem[a]=text.count(a)
    print(a)
    print(text.count(a))

print(tulem)

import operator

sorditud = sorted(tulem.items(), key=operator.itemgetter(1), reverse=True)

print(sorditud)


