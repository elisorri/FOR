hastafir = 0
lagstafir = 0
lagEftirHa = 0
texti = input("Sláðu inn texta ")
for i in range(len(texti)):
    if(texti[i].isalpha() and texti[i].isupper()):
        hastafir = hastafir + 1
        if(texti[i + 1].islower()):
            lagEftirHa = lagEftirHa + 1
    if(texti[i].isalpha() and texti[i].islower()):
        lagstafir = lagstafir + 1
print("Það eru", hastafir, "hástafir", ",", lagstafir, "lágstafir og", lagEftirHa, "lágstafir koma beint á eftir hástaf")