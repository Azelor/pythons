"""
Defineerida funktsioon risk(pakki_paevas, suitsetatud_aastaid), mis tagastab
kopsuhaiguse riskikoefitsendi. Parameetrid pakki_paevas ja suitsetatud_aastaid on
reaalarvud.
Juhul kui suitsetatud_aastaid on suurem kui 10, siis on riskikoefitsent pakki_paevas2
.
Muul juhul on riskikoefitsent pakki_paevas/3.
"""


# Defineerin funktsiooni risk
def risk(pakki_paevas, suitsetatud_aastaid):
    if suitsetatud_aastaid > 10:
        # Kui suitstetatud_aastaid on rohkem kui 10, siis on tulemiks (pakki_paevas)^2
        return pakki_paevas**2
    else:
        # Vastasel juhul on tulemiks pakki_paevas/3
        return pakki_paevas/3
