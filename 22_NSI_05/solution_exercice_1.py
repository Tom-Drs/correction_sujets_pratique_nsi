def RechercheMinMax(tab: list):
    if len(tab) == 0:
        return {"min": None, "max": None}
    minimum = tab[0]
    maximum = tab[0]
    for valeur in tab:
        if valeur < minimum:
            minimum = valeur
        if valeur > maximum:
            maximum = valeur
    return {"min": minimum, "max": maximum}


# Attention ici dans les exemples la fonction doit bien avoir une majuscule.
assert RechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert RechercheMinMax([]) == {'min': None, 'max': None}
