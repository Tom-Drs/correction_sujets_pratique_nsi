def fusion(tab1: list, tab2: list) -> list:
    index_1 = 0
    index_2 = 0
    liste_fusion = []
    while index_1 < len(tab1) and index_2 < len(tab2):
        if tab1[index_1] < tab2[index_2]:
            liste_fusion.append(tab1[index_1])
            index_1 += 1
        else:
            liste_fusion.append(tab2[index_2])
            index_2 += 1
    while index_1 < len(tab1):
        liste_fusion.append(tab1[index_1])
        index_1 += 1
    while index_2 < len(tab2):
        liste_fusion.append(tab2[index_2])
        index_2 += 1
    return liste_fusion

assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]