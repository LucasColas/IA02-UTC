%On considère une liste de dominos, chacun d’eux étant représenté par la liste [I, J] 
%des deux chiffres qu’il porte. On cherche à les aligner, selon le procédé habituel :

    %-Un domino peut être ajouté à l’une des deux extrémités de la suite déjà construite.
    %-Les deux faces en contact doivent porter le même chiffre.
    %-On peut retourner un domino.


%Question 1

%Écrire un prédicat suite_domino(+A_placer, -Suite) qui, étant donné une liste de dominos A_placer, 
%unifie avec Suite une suite légale de dominos utilisant tous les dominos à placer.
permutate_elements([X,Y], [X,Y]).
permutate_elements([X,Y], [Y,X]).

permutate_lists([], []).
permutate_lists([L|Ls], [P|Ps]) :-
    permutation(L, P),
    permutate_lists(Ls, Ps).

suite_domino(A_placer, Suite) :-
    permutate_lists(A_placer, P),
    maplist(permutate_elements, P, Suite).

%Question 2
%Créer un prédicat générateur dominos(-D) qui génère l’ensemble des dominos possibles.

%On pourra utiliser pour cela le prédicat prédéfini between(+Low, +High, ?Value) qui peut être utilisé comme générateur de nombres entiers.

domino(D) :-
    between(0,6,X),
    between(0,6,Y),
    D = [X,Y].