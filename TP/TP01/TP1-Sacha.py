def decomp(n, nb_bits):
    if n > (2**nb_bits-1) and nb_bits <= 0:
        # Erreur nombre trop grand
        return -1
    temp = n
    binary_conv = []
    while temp:
        binary_conv.append(temp%2==1)
        temp //= 2

    binary_conv.reverse()

    while len(binary_conv) < nb_bits:
        binary_conv.insert(0, False)

    return binary_conv


def interpretation(voc, vals):
    if len(voc) != len(vals):
        #Erreur
        return -1

    dico = {}
    for vo, val in zip(voc, vals):
        dico[vo] = val

    return dico


def gen_interpretations(voc):
    nb_bits = len(voc)
    for i in range(2**nb_bits):
        yield interpretation(voc, decomp(i, nb_bits))


def valuate(formula, interpretation):
    return eval(formula, interpretation)


def table(formula, voc):
    def my_line():
        for _ in voc:
            print("+---", end="")
        print("+-------+")

    list_interpretation = gen_interpretations(voc)

    print("formule : " + formula)

    my_line()

    for elt_voc in voc :
        print("| " + elt_voc + " ", end="")
    print("| eval. |")

    my_line()

    for interpretation in list_interpretation:
        for val in interpretation.values():
            print("| "+str(val)[0]+" ", end="")
        print("|   " + str(valuate(formula, interpretation))[0] + "   |")

    my_line()


def valide(formula, voc):
    list_interpretation = gen_interpretations(voc)

    for interpretation in list_interpretation:
        if not valuate(formula, interpretation):
            return False

    return True


def contradictoire(formula, voc):
    list_interpretation = gen_interpretations(voc)

    for interpretation in list_interpretation:
        if valuate(formula, interpretation):
            return False

    return True


def contingente(formula, voc):
    return not (valide(formula, voc) or contradictoire(formula, voc))


def is_cons(f1, f2, voc):
    liste_interpretation = gen_interpretations(voc)
    for inter in liste_interpretation:
        if valuate(f1, inter) and not valuate(f2, inter):
            return False

    return True


def main ():
    print(is_cons("p and q", "p or q", ["p", "q"]))


if __name__ == "__main__":
    main()
