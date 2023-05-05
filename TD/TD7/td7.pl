%Exercice listes
%1.tete(+L, -H) qui unifie la variable H avec la tête de la liste L.
tete(L, H) :-
    L = [H|_].
    
%2.reste(+L, -R) qui unifie la variable R avec le reste de la liste L
reste(L, R) :-
    L = [_|R].

%3.vide(+L) qui est vrai si la liste L est vide.
vide(L) :-
    L = [].

%4.element(?X, ?L) qui est vrai si X est présent dans la liste L.
element(_, []) :-
    false.

element(X, L) :-
    L = [A|_],
    X = A.

element(X, L) :-
    L = [A|R],
    dif(X,A),
    element(X, R).

%5.dernier(+L, -X) qui unifie X avec le dernier élément de la liste L.
dernier(L, X) :-
    L = [X].
dernier(L, X) :-
    L = [_|R],
    dernier(R, X).

%6.longueur(+L, -Lg) qui unifie Lg avec la longueur de la liste L.
longueur([], 0).
longueur(L, Lg) :-
    L = [_|R],
    longueur(R, Lg2),
    Lg is Lg2 + 1.

%7.nombre(+L, +X, ?N) qui compte le nombre de fois où X apparaît dans L et unifie le résultat avec N.
nombre([], _, 0).
nombre(L, X, N) :-
    L = [A|R],
    X = A,
    nombre(R, X, N2),
    N is N2 + 1.
nombre(L, X, N) :-
    L = [A|R],
    dif(X, A),
    nombre(R, X, N).

%8.concat(+L1, +L2, -L3) qui effectue la concaténation de la liste L1 avec la liste L2 et l’unifie avec L3.
concat([], L2, L2).
concat(L1, L2, L3) :-
    L1 = [A|R],
    concat(R, L2, L32),
    L3 = [A|L32].

%9.inverse(+L, -R) telle que la liste R soit l’inverse L.
inverse([], []).
inverse(L, R) :-
    L = [A|R1],
    inverse(R1, R2),
    concat(R2, [A], R).

%10.sous_liste(+L1, +L2) qui vérifie que L1 est une sous liste de L2.

%sous_liste([], _).

%sous_liste(_, []).

%sous_liste(L1, L2) :-
    %L1 = [A|R1],
    %L2 = [B|R2],
    %A = B,
    %sous_liste(R1, R2).

%sous_liste(L1, L2) :-
    %L1 = [A|R1],
    %L2 = [B|R2],
    %dif(A, B),
    %sous_liste(L1, R2).

debute_par(_,[]).
debute_par([H|R1], [H|R2]) :-
    debute_par(R1, R2).

sous_liste([T|R1], [T|R2]) :-
    debute_par(R1, R2).

sous_liste([_|R1], R2) :-
    sous_liste(R1, R2).

    
%11.retire_element(+L, +X, -R) qui retire la première occurrence de l’élément X dans L et place le résultat dans R.
retire_element([], _, []).
retire_element(L, X, R) :-
    L = [A|R1],
    X = A,
    R = R1.


retire_element(L, X, R) :-
    L = [A|R1],
    dif(X, A),
    retire_element(R1, X, R2),
    R = [A|R2].


%Ex2
%1.Définir partition(+X, +L, -L1, -L2) qui place dans L1 les éléments de L qui sont 
%inférieurs ou égaux à X, et dans L2 les éléments de L qui sont strictement supérieurs à X.
partition(_, [], [], []).
partition(X, L, L1, L2) :-
    L = [A|R],
    A =< X,
    partition(X, R, L11, L2),
    L1 = [A|L11].

partition(X, L, L1, L2) :-
    L = [A|R],
    A > X,
    partition(X, R, L1, L22),
    L2 = [A|L22].

%2.Définir tri(+L1, ?L2) qui trie la liste L1 et unifie le résultat avec L2
tri([], []).
tri(L1, L2) :-
    L1 = [A|R],
    partition(A, R, L11, L12),
    tri(L11, L111),
    tri(L12, L122),
    concat(L111, [A|L122], L2).


%Ex3
%On souhaite représenter les ensembles en Prolog comme des listes sans doublons. Définir l’ensemble des prédicats suivants.
%1.retire_elements(+X, +L, -R) qui retire toutes les occurrences de X dans L et place le résultat dans R.
retire_elements(_, [], []).
retire_elements(X, L, R) :-
    L = [A|R1],
    X = A,
    retire_elements(X, R1, R).
    

retire_elements(X, L, R) :-
    L = [A|R1],
    dif(X, A),
    retire_elements(X, R1, R2),
    R = [A|R2].

%2.retire_doublons(+L, -E) qui transforme la liste L en un ensemble E (sans redondance).
retire_doublons([], []).
retire_doublons(L, E) :-
    L = [A|R],
    retire_elements(A, R, R2),
    retire_doublons(R2, E2),
    E = [A|E2].

%3.union(+E1, +E2, -E) qui effectue l’union de l’ensemble E1 avec l’ensemble E2 et place le résultat dans E.
union([], E2, E2).
union(E1, [], E1).
union(E1, E2, E) :-
    E1 = [A|R1],
    E2 = [_|R2],
    retire_elements(A, E2, R3),
    union(R1, R3, E3),
    E = [A|E3].

%4.intersection(+E1, +E2, -E) qui effectue l’intersection de l’ensemble E1 avec l’ensemble E2 et place le résultat dans E.

intersection([], _, []).
intersection(_, [], []).
intersection(E1, E2, E) :-
    E1 = [A|R1],
    element(A, E2),
    intersection(R1, E2, E3),
    E = [A|E3].

intersection(E1, E2, E) :-
    E1 = [A|R1],
    \+element(A, E2),
    intersection(R1, E2, E3),
    E = E3.
    
    
