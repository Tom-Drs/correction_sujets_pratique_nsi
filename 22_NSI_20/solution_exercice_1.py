
def xor(tab1: list, tab2: list):
    resultat = []
    for index in range(len(tab1)):
        if tab1[index] == tab2[index]:
            resultat.append(0)
        else:
            resultat.append(1)
        # resultat.append(int(not tab1[index] == tab2[index])) petit tricks qui permet de d'enlever la structure conditionnelle (juste pour flex).
    return resultat


a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]

assert(xor(a, b) == [1, 1, 0, 1, 1, 0, 0, 1])
assert(xor(c, d) == [1, 1, 1, 0])