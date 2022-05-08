
def nombre_de_mots(phrase: str) -> int:
    compteur = 0
    for caractere in phrase:
        if caractere == " " or caractere == ".":
            compteur += 1
    return compteur

assert nombre_de_mots('Le point d exclamation est separe !') == 6
assert nombre_de_mots('Il y a un seul espace entre les mots !') == 9
assert nombre_de_mots('Il y a un seul espace entre les mots.') == 9