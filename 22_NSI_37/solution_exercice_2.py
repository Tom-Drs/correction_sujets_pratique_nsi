urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if resultat.get(bulletin) is not None:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat.update({bulletin: 1})
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale


urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
assert depouille(urne) == {'B': 4, 'A': 3, 'C': 3}
assert vainqueur(depouille(urne)) == ["B"]
## Les exemples sont faux ici quels bande de noobs l'éducation nationnal