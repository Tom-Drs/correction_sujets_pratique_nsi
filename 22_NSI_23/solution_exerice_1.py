def max_dico(dico: dict) -> tuple:
    plus_grande_cle = list(dico.keys())[0]
    for key, value in dico.items():
        if value > dico.get(plus_grande_cle):
            plus_grande_cle = key
    return plus_grande_cle, dico.get(plus_grande_cle)


assert max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}) == ('Ada', 201)
assert max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}) == ('Alan', 222)