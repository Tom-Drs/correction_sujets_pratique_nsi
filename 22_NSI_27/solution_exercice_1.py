def taille(arbre: dict, lettre: str) -> int:
    if lettre == "":
        return 0
    return taille(arbre, arbre.get(lettre)[0]) + taille(arbre, arbre.get(lettre)[1]) + 1

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}

assert taille(a, "F") == 9