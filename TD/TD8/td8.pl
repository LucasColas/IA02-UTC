%Problème 1

%1.Définir un prédicat chiffre(?X) qui est vrai si X 
%est un chiffre. On utilisera pour cela element/2 
%dans le TD précédent (ou le prédicat prédéfini member/2)
element(_, []) :-
    false.

element(X, L) :-
    L = [A|_],
    X = A.

element(X, L) :-
    L = [A|R],
    dif(X,A),
    element(X, R).
chiffre(X) :-
    element(X, [0,1,2,3,4,5,6,7,8,9]).

%2.Définir le prédicat generate(-X1, -X2) qui 
%générera l’ensemble des couples ordonnés de chiffres (X1, X2).
generate(X1, X2) :-
    chiffre(X1),
    chiffre(X2).

%3.Définir un prédicat test(+X1, +X2, +X) qui teste les 2 
%contraintes de l’énoncé pour les 2 nombres générés.
test(X1, X2, X) :-
    X is X1 + X2,
    dif(X1,X2).


%Problème 2 : Les Maisons
%1.Définir le prédicat solve([?M1, ?M2, ?M3]) permettant de résoudre le problème. 
%On utilisera pour cela l’algorithme generate and test.
