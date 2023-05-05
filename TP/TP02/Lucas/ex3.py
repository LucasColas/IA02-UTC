def obtenir_clauses(sommets, arcs, couleurs):
    clauses = []
    mapping_sommet = {}
    num = 1
    for sommet in sommets:
        clauses.append(["S" + str(sommet)+ str(couleur) for couleur in couleurs])
        for couleur in couleurs:
            mapping_sommet["S"+str(sommet)+couleur] = num
            num += 1

            for couleur2 in couleurs:
                if couleur != couleur2:
                    clauses.append(["-S" + str(sommet) + couleur, "-S" + str(sommet) + couleur2])

    for arc in arcs:
        for couleur in couleurs:
            clauses.append(["-S" + str(arc[0]) + couleur, "-S" + str(arc[1]) + couleur])


    for clause in clauses:
        for i in range(len(clause)):
            if clause[i][0] == "-":
                clause[i] = "-" + str(mapping_sommet[clause[i][1:]])
            else:
                clause[i] = str(mapping_sommet[clause[i]])

    return clauses

def main():
    couleurs = ["R", "V", "B"] #1 : R, 2 : Vert, 3 : Bleu
    nb_sommets = 10
    sommets = [i for i in range(1, nb_sommets+1)]
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

    clauses = obtenir_clauses(sommets, arcs, couleurs)

    f = open("coloration.cnf", "w")
    f.write("c Coloration d'un graphe\n")
    f.write("c\n")
    f.write("c Nombre de sommets: " + str(nb_sommets) + "\n")
    f.write("c Nombre de couleurs: " + str(len(couleurs)) + "\n")
    f.write("c\n")
    f.write("p cnf " + str(nb_sommets * len(couleurs)) + " " + str(len(clauses)) + "\n")


    ## Clauses
    for clause in clauses:
        f.write(" ".join(clause) + " 0\n")

    f.close()





if __name__ == "__main__":
    main()
