while True:
    try:
        arv = int(input("Siseta arv:  "))
        print(arv)
        break
    except ValueError:
        print("Vale sisend! Palun sisesta arv:  ")
    except:
        print("Ootamatu viga!!")
