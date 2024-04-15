import itertools

def evaluer_expression(expression, variables):
    valeurs_verite = []
    for combinaison in itertools.product([False, True], repeat=len(variables)):
        valeurs = dict(zip(variables, combinaison))
        valeur = eval(expression, valeurs)
        valeurs_verite.append((combinaison, valeur))
    return valeurs_verite

def afficher_table_verite(expression, variables):
    valeurs_verite = evaluer_expression(expression, variables)
    print("Table de vérité pour l'expression :", expression)
    print("-" * (len(expression) + 18))
    for var in variables:
        print(f"| {var} ", end='')
    print("| Résultat |")
    print("-" * (len(expression) + 18))
    for combinaison, valeur in valeurs_verite:
        for val in combinaison:
            print(f"| {int(val)} ", end='')
        print(f"| {int(valeur)} ".center(len(expression) + 10) + "|")
    print("-" * (len(expression) + 18))

def calculer_formes_canoniques(expression, variables):
    formes_canoniques = []
    valeurs_verite = evaluer_expression(expression, variables)
    for combinaison, valeur in valeurs_verite:
        if valeur:
            termes = []
            for var, val in zip(variables, combinaison):
                termes.append(f"({var} and not {val})" if not val else f"({var} and {val})")
            formes_canoniques.append(" or ".join(termes))
        else:
            termes = []
            for var, val in zip(variables, combinaison):
                termes.append(f"({var} and {val})" if val else f"({var} and not {val})")
            formes_canoniques.append(" and ".join(termes))
    return formes_canoniques

expression = input("Entrez l'expression logique (utilisez les opérateurs logiques Python): ")
variables = input("Entrez les variables séparées par des espaces: ").split()

afficher_table_verite(expression, variables)

formes_canoniques = calculer_formes_canoniques(expression, variables)
print("\nForme canonique (première forme):")
print(" or ".join(formes_canoniques))

formes_canoniques.reverse()
print("\nForme canonique (deuxième forme):")
print(" and ".join(formes_canoniques))