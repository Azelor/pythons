def lineaar_fn(n, a, b):
    "Defineeri funktsioon lineaar_fn"
    # Loo tühi loend tulemi jaoks
    tulem = []
    for i in range(n):
        # Tee for-tsükkel, mis lisab sõltuvalt n-st, tulemisse väärtuse b
        tulem.append(b)
        # Suurenda väärtust b väärtuse a võrra
        b += a
    # Tagasta tulem
    return tulem
        
