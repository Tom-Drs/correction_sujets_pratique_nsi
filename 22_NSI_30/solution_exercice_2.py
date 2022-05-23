def rom_to_dec(nombre):
    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    dico = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(nombre) == 1:
        return dico.get(nombre)
    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
        ### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]

        if dico[nombre[0]] >= dico[nombre[1]]:
            return dico[nombre[0]] + rom_to_dec(nombre[1:])
        else:
            return rom_to_dec(nombre[1:]) - dico[nombre[0]]


assert rom_to_dec("CXLII") == 142
assert rom_to_dec("CDIII") == 403
assert rom_to_dec("XVI") == 16
