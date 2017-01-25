#Elís Orri

hastafir = 0
lagstafir = 0
lagEftirHa = 0
#Forrit biður um texta
texti = input("Sláðu inn texta ")
#Forrit reiknar ú hvað eru margir hástafir og lágstafir og hve margir lágstafir koma beint á eftir hástöfum
for i in range(len(texti)):
    if(texti[i].isalpha() and texti[i].isupper()):
        hastafir = hastafir + 1
        if(texti[i + 1].islower()):
            lagEftirHa = lagEftirHa + 1
    if(texti[i].isalpha() and texti[i].islower()):
        lagstafir = lagstafir + 1
#Forrit birtir niðurstöður
print("Það eru", hastafir, "hástafir", ",", lagstafir, "lágstafir og", lagEftirHa, "lágstafir koma beint á eftir hástaf")