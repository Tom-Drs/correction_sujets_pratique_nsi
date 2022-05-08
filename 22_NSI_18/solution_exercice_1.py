def mini(releve: list, date: list) -> tuple:
    index_plus_petit = 0
    for index in range(len(releve)):
        if releve[index] < releve[index_plus_petit]:
            index_plus_petit = index
    return releve[index_plus_petit], date[index_plus_petit]


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
assert mini(t_moy, annees) == (12.5, 2016)
