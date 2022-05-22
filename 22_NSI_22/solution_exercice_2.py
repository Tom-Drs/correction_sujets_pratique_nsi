def crible(N):
    """renvoie un tab contenant tous les nombres premiers plus petit que N"""
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(2, N):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2*i, N, i):
                tab[multiple] = False
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


# Si tu veux flex un maximum et faire une fonction qui trouve les n nombres premiers en une ligne
nombres_premiers = lambda x: [i for i in range(x+1) if sum(1 if i % div == 0 else 0 for div in range(1, i+1)) == 2]

