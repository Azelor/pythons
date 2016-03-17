def char_frequencies(text):
    tulem = {}
    for i in text:
        tulem[i] = tulem.get(i, 0) + 1
    return tulem
