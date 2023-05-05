couleur = ["R", "V", "B"]
nb_sommets = 10
points = [i for i in range(1, nb_sommets + 1)]
arcs = [
    [1, 3],
    [1, 4],
    [1, 6],
    [2, 4],
    [2, 5],
    [2, 7],
    [3, 5],
    [3, 8],
    [4, 9],
    [5, 10],
    [6, 7],
    [7, 8],
    [8, 9],
    [9, 10],
    [10, 6]
]


def main():
    # Pour chaque sommet dire qu'il n'a qu'une seule couleur
    clauses = []
    dict_sommet = {}
    compteur_sommet = 1

    for sommet in points:
        clauses.append(["S" + str(sommet) + coul for coul in couleur])
        for coul1 in couleur:
            dict_sommet["S" + str(sommet) + coul1] = compteur_sommet
            compteur_sommet += 1
            for coul2 in couleur:
                if coul1 != coul2:
                    clauses.append(["-S" + str(sommet) + coul1,
                                   "-S" + str(sommet) + coul2])

    # Pour chaque arc dire que les sommets n'ont pas la même couleur
    for arc in arcs:
        for coul in couleur:
            clauses.append(["-S" + str(arc[0]) + coul,
                           "-S" + str(arc[1]) + coul])

    # Remplacer les sommets par leurs numéros dans les clauses
    for clause in clauses:
        for i in range(len(clause)):
            if clause[i][0] == "-":
                clause[i] = "-" + str(dict_sommet[clause[i][1:]])
            else:
                clause[i] = str(dict_sommet[clause[i]])

    # Écriture du fichier

    # Commentaires
    file = open("coloration.cnf", "w")
    file.write("c Coloration d'un graphe\n")
    file.write("c\n")
    file.write("c Nombre de sommets: " + str(nb_sommets) + "\n")
    file.write("c Nombre de couleurs: " + str(len(couleur)) + "\n")
    file.write("c\n")
    file.write("p cnf " + str(nb_sommets * len(couleur)) +
               " " + str(len(clauses)) + "\n")

    # Clauses
    for clause in clauses:
        file.write(" ".join(clause) + " 0\n")

    file.close()

    afficher_solution(dict_sommet)


def afficher_solution(dict_sommet_coul):
    """
    Permet d'afficher la couleur de chaque sommet solution
    Ainsi à partir de la liste des valeurs de la solution, on remplace les numéros par les couleurs
    """

    print("Veuillez saisir la solution :")
    solution = input()

    if solution == "0":
        print("Pas de solution")
        return

    solution = solution.split(" ")
    solution = solution[1:-1]

    # Découpage de la solution par groupe de 3
    solution = [solution[i:i+3] for i in range(0, len(solution), 3)]

    # On ne garde que les valeurs positives dans chaque groupe et on les transforme en entier en les ajoutant à une liste de solution
    couleur_solution = []
    for clause in solution:
        for i in range(len(clause)):
            if clause[i][0] != "-":
                couleur_solution.append(int(clause[i]))

    # On remplace les numéros par les couleurs
    for i in range(len(couleur_solution)):
        for key, value in dict_sommet_coul.items():
            if couleur_solution[i] == value:
                couleur_solution[i] = key
                break


if __name__ == "__main__":
    main()
