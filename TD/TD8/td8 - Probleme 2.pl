%Problème 2 : Les Maisons
%1.Définir le prédicat solve([?M1, ?M2, ?M3]) permettant de résoudre le problème. 
%On utilisera pour cela l’algorithme generate and test.

% Couleurs des maisons
couleur(bleu).
couleur(vert).
couleur(rouge).

% Nationalités des habitants
nationalite(italien).
nationalite(norvegien).
nationalite(espagnol).

element(_, []) :- 
    false.

element(X, L) :-
    L = [A|_],
    X = A.

element(X, L) :-
    L = [A|R],
    dif(X,A),
    element(X, R).

nummaison(M) :-
    element(M, [1,2,3]).

generate([M1, M2, M3]) :-
    nummaison(M1),
    nummaison(M2),
    nummaison(M3),
    dif(M1, M2),
    dif(M1, M3),
    dif(M2, M3).


solve(M1, M2, M3) :-
    
