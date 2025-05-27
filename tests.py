#!/usr/bin/python3

def chiffres_uniques(n):
    chaine = str(n)
    compteur = {}
    for chiffre in chaine:
        if chiffre in compteur:
            compteur[chiffre] +=1
        else:
            compteur[chiffre] = 1
    
    resultats = []
    for chiffre in chaine:
        if compteur[chiffre] == 1:
            resultats.append(int(chiffre))
    
    return resultats

print(chiffres_uniques(1122335))