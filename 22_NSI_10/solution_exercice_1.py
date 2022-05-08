
def occurence_lettres(phrase: str) -> dict:
    dictionnaire_occurences = {}
    for caractere in phrase:
        if dictionnaire_occurences.get(caractere) is None:
            dictionnaire_occurences.update({caractere: 1})
        else:
            dictionnaire_occurences[caractere] += 1
    return dictionnaire_occurences

occurence_lettres("Hello world !") == {'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}