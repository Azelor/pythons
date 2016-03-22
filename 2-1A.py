"""
Defineerida funktsioon mutatsiooni_tn(rad), mille parameetriks on kiiritusdoos rad ja
mis tagastab reaalarvulise mutatsiooni tõenäosuse vahemikus 0..1. Juhul kui rad on väiksem kui 25
on tõenäosus 0. Vastasel juhul on tõenäosuseks rad/(rad+1000)
"""


# Defineerin funktsiooni mutatsiooni_tn
def mutatsiooni_tn(rad):
    # Kui rad on väiksem kui 25, siis on tulemiks 0
    if rad < 25:
        return 0
    # Vastasel juhul on tulemiks arv, kasutades etteantud võrrandit
    else:
        return (rad/(rad+1000))
