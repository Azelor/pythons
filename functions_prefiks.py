""" Defineerida funktsioon korduv_prefiks(s, n, m), millel on kolm parameetrit:
s: string
n: täisarv, prefiksi pikkus
m: täisarv, korduste arv."""


def korduv_prefiks(s, n, m):
    "Sisesta string, prefiksi pikkus ja prefiksi korduste arv"
    return s[:n] * int(m)
    
