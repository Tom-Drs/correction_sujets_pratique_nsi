def recherche(caractere: str, mot: str) -> int:
    compteur_occurence = 0
    for lettre in mot:
        if lettre == caractere:
            compteur_occurence += 1
    return compteur_occurence


assert recherche('e', "sciences") == 2
assert recherche('i', "mississippi") == 4
assert recherche('a', "mississippi") == 0
