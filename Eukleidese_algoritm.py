def gcd(a, b):
    "Arvude a ja b suurim ühistegur"
    #Tsükkel kestab kuni b on nullist suurem
    while b > 0:232
        r = a % b
        a = b
        b = r
    return(a)
        
