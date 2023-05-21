%On considère une liste de dominos, chacun d’eux étant représenté par la liste [I, J] 
%des deux chiffres qu’il porte. On cherche à les aligner, selon le procédé habituel :

    %-Un domino peut être ajouté à l’une des deux extrémités de la suite déjà construite.
    %-Les deux faces en contact doivent porter le même chiffre.
    %-On peut retourner un domino.


%Question 1

%Écrire un prédicat suite_domino(+A_placer, -Suite) qui, étant donné une liste de dominos A_placer, 
%unifie avec Suite une suite légale de dominos utilisant tous les dominos à placer.

suite_domino([], []).
suite_domino([D], [D]).
suite_domino([[X,Y]], [[Y, X]]) :- dif(X, Y).

suite_domino(A_placer, [[X1,Y1], [X2,Y2] | R]) :-
    select([X1,Y1], A_placer, A_placer2),
    Y1 = X2,
    suite_domino(A_placer2, [[X2,Y2] | R]).

suite_domino(A_placer, [[Y1,X1], [X2,Y2] | R]) :-
    dif(X1, Y1),
    select([X1,Y1], A_placer, A_placer2),
    X1 = X2,
    suite_domino(A_placer2, [[X2,Y2] | R]).


%Question 2
%Créer un prédicat générateur dominos(-D) qui génère l’ensemble des dominos possibles.

%On pourra utiliser pour cela le prédicat prédéfini between(+Low, +High, ?Value) qui peut être utilisé comme générateur de nombres entiers.

range(Start, _, Start).
range(Start, End, Value) :-
    Start < End,
    NewStart is Start + 1,
    range(NewStart, End, Value).

gen(N, [X,Y]) :-
    range(0, N, X),
    range(0, N, Y).

test([X,Y]) :-
    X =< Y.

dominos(X) :-
    gen(6, X),
    test(X).


%Question 3
%Utiliser les deux questions précédentes et le prédicat findall(+Template, :Goal, -Bag), donner la requête permettant de trouver toutes les suites possibles avec un jeu entier de dominos.
%Générer toutes dominos avec un jeu de dominos de 6.
%Puis donner toutes les suites possibles.
generer_dominos(D) :-
    findall(X, dominos(X), E),
    suite_domino(E,D).