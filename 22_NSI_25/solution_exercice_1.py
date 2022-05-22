animaux = [
    {"nom": "Medor", "espece": "chien", "age": 5, "enclos": 2},
    {"nom": "Titine", "espece": "chat", "age": 2, "enclos": 5},
    {"nom": "Tom", "espece": "chat", "age": 7, "enclos": 4},
    {"nom": "Belle", "espece": "chien", "age": 6, "enclos": 3},
    {"nom": "Mirza", "espece": "chat", "age": 6, "enclos": 5},
]


def selection_enclos(table_animaux: list, num_enclos: int) -> list:
    resultat = []
    for animal in table_animaux:
        if animal.get("enclos") == num_enclos:
            resultat.append(animal)
    return resultat


assert selection_enclos(animaux, 5) == [
    {'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5},
    {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]
assert selection_enclos(animaux, 2) == [
    {'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2}]
assert selection_enclos(animaux, 7) == []
