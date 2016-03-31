from random import randint

def veeretus():
    tulem = randint(1, 20)
    print("Sinu veeretus:", tulem)
    return tulem

def puuviljavaagen():
    print("Oled apelsin puuviljavaagnas, kes on äkitselt omandanud mõtlemisvõime.")
    print("Näed perenaist, käes nuga, sirutamas kätt sinu suunas.")

    sisend = input("Sinu valik (a, b): \n (a) Oota ja vaata, mis juhtub. \n (b) Veere vaagnalt maha põrandale.\n")
    
    if sisend == "a":
        # Kui mängija ootab...
        print("Perenaine koorib sul naha maha ja teeb su sisemusest mahla. Vähemalt kellegi tuju tegid sa heaks.")
    elif sisend == "b":
        # Kui mängija otsustab veereda...
        v = veeretus()
        print("Veereta vähemalt 10!")
        if v >= 10:
              print("Suutsid end laualt maha veeretada enne kui perenaine sai aru, mis toimub!")
              p6rand()
        else:
              print("Perenaine pistab liigutava apelsini peale kiljuma ja lööb sind noaga. \nÕnneks valu sa ei tunne, sest oled apelsin.")
    else:
        # Kui vale sisend...
        print("Vale sisend. Perenaine viskab su prügikasti. Milline tänamatus!")
        print("Järgmine kord vali a või b.")

def p6rand():
    print("Oled köögipõrandal. Perenaine on liikuva apelsini tõttu hüsteerias. \nPead põgenema!")
    sisend = input("Sinu valik (a, b): \n (a) Vasakul asuv klapiga kassi uks. \n (b) Radiaatori alune \n")
    if sisend == "a":
        # Kui veered õue...
        print("Veered kassi ukse kaudu majast välja.")
        majaesine()
    elif sisend == "b":
        # Kui lähed radika alla...
        print("Veered radika alla ilma, et perenaine sind näeks. \nKuivad kokku ja täidab maja meeldiva tsitrusearoomiga.")
    else:
        # Kui vale sisend...
        print("Vale sisend. Perenaine astub sulle peale. Milline tänamatus!")
        print("Järgmine kord vali a või b.")

def majaesine():
    print("Jõudsid õue. Näed enda poole jooksmas suurt koera!")
    sisend = input("Sinu valik (a, b): \n (a) Põgened tänaval asuvasse rentslisse! \n (b) Oled julge ja võitled koeraga! \n")
    if sisend == "a":
        # Kui põgened rentslisse..
        print("Üritad koerast kiirem olla. Veereta vähemalt 12!")
        v = veeretus()
        if v >= 12:
              print("Suutsid koera hammustustest kõrvale põigelda ja rentslisse põgeneda.")
              rentsel()
        else:
              print("Koer näris su puruks. Milline tänamatus!")
        
    elif sisend == "b":
        # Kui oled julge...
        print("Kavatsed koerale näidata, kes siin peremees on! Veereta vähemalt 17!")
        v = veeretus()
        if v >= 17:
              print("Keegi ei tea täpselt kuidas, aga sul õnnestus lahingus koera võita. Nüüd oled sina aia peremees. \nVäravale kinnitatakse uus silt: Ettevaatust, kuri apelsin!")
        else:
              print("Koer näris su puruks. Milline tänamatus!")

def rentsel():
    print("Kanalistatsioonitorustik on kole koht. Isegi apelsinide arvates.")
    print("Hea õnne korral viib vool sind merre. Veereta 20")
    v = veeretus()
    if v == 20:
        print("Sul vedas tohutult ja peale suurt seiklust jõudsid lõpuks merre, kus on apelsinide koht.")
    else:
        print("Saatuse tahtel kõdunesid rentslis. Kes teab, järgmises elus läheb ehk paremini...")


#Peafunktsioon
puuviljavaagen()
