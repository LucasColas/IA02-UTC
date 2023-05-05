def decomp(n, nb_bits):
    """
    étant donné un nombre n, calcule la décomposition binaire en nb_bits de n.
    L’ordre des bits (croissant ou décroissant) est sans importance.
    """
    a = []
    while(n>0):
        dig=n%2
        if dig:
            a.append(True)
        else:
            a.append(False)
        n=n//2

    a.reverse()
    while len(a) < nb_bits:
        a.insert(0,False)
    return a

def interpretation(voc, vals):

    """
     fonction qui, étant donné un tableau de chaîne de caractère
     représentant les variables propositionnelles et un liste
     de valeurs prises par ces variables renvoie une interprétation.

    """
    if len(voc) != len(vals):
        return -12

    dic = {}

    for i in range(len(voc)):
        dic[voc[i]] = vals[i]

    return dic

def gen_interpretations(voc):
    """
    étant donné la liste des variables booléennes, génère une à une les interprétations.
    """
    nb = len(voc)
    for i in range(2**nb):
        yield interpretation(voc, decomp(i, nb))

def valuate(formula, interpretation):
    """
    prenant en entrée une chaîne de caractères représentant la
    formule à évaluer et une interprétation et qui renvoie True ou False
    """
    return eval(formula, interpretation)


#essai = gen_interpretations(["A", "B", "C", "D"])
#valuate_ = valuate("(A or B) and not(C)", {"A": True, "B": False, "C": False})


def table(formula, voc):
    """
    Écrire une fonction permettant d’afficher la table de vérité
    étant donné une formule propositionnelle et le vocabulaire afférent.
    """
    gen = gen_interpretations(voc)
    for g in gen:
        for val in g.values():
            print(str(val)[0] + ' ', end='')

        print(str(valuate(formula, g))[0])
        print()

#table("(A or B) and not(C)", ["A", "B", "C"])



def est_valide(formula, voc):
    """
    vérifie si une formule est valide.
    """
    gen = gen_interpretations(voc)
    for g in gen:
        if not valuate(formula, g):
            return False
    return True

def est_contradictoire(formula, voc):
    """
    vérifie si une formule est contradictoire.
    """
    gen = gen_interpretations(voc)
    for g in gen:
        if valuate(formula, g):
            return False

    return True

def est_contingent(formula, voc):
    """
    vérifie si une formule est contingente
    """
    return not (est_valide(formula, voc) or est_contradictoire(formula, voc))

def is_cons(f1, f2, voc):
    gen = gen_interpretations(voc)
    for g in gen:
        if valuate(f1, g) and not valuate(f2, g):
            return False

    return True

def main ():
    print(is_cons("p and q", "p or q", ["p", "q"]))


if __name__ == "__main__":
    main()
