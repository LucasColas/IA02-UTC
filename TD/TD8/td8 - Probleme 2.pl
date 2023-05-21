%Problème 2 : Les Maisons
%On souhaite trouver une solution via Prolog au problème suivant. Dans une rue sont alignées 3 maisons, numérotées de gauche à droite de 1 à 3. Dans chaque maison habite une unique personne. On veut connaître la couleur de chaque maison et la nationalité de chacun des habitants.

    %Règle 1 : Chaque maison possède une couleur différente (bleu, vert ou rouge).
    %Règle 2 : Chaque habitant possède une nationalité différente (Italien, Norvégien ou Espagnol).


    %Indice 1 : L’Espagnol habite la maison directement à droite de la maison rouge.
    %Indice 2 : Le Norvégien vit dans la maison bleue.
    %Indice 3 : L’Italien habite dans la maison n°2.

%1.Définir le prédicat solve([?M1, ?M2, ?M3]) permettant de résoudre le problème. 
%On utilisera pour cela l’algorithme generate and test.
element(_, []) :-
    false.

element(X, L) :-
    L = [A|_],
    X = A.

element(X, L) :-
    L = [A|R],
    dif(X,A),
    element(X, R).

% Numéro des maisons
numero(X) :- member(X, [1,2,3]).

% Couleur des maisons
couleur(X) :- member(X, [bleu, vert, rouge]).

% Nationalité
nationalite(X) :- member(X, [italien, norvegien, espagnol]).

generate([maison(Num1, Coul1, Nat1), maison(Num2, Coul2, Nat2),maison(Num3, Coul3, Nat3)]) :-
    numero(Num1), couleur(Coul1), nationalite(Nat1),
    numero(Num2), couleur(Coul2), nationalite(Nat2),
    numero(Num3), couleur(Coul3), nationalite(Nat3). 

dif3(X, Y, Z) :-
    dif(X,Y),
    dif(X,Z),
    dif(Y,Z).

% Dans une rue sont alignées 3 maisons, numérotées de gauche à droite de 1 à 3. 
regle0() :-
    generate([maison(1, _, _), maison(2, _, _), maison(2, _, _)]).

% Chaque maison possède une couleur différente (bleu, vert ou rouge).
regle1() :-
    generate([maison(_, Coul1, _), maison(_, Coul2, _), maison(_, Coul3, _)]),
    dif3(Coul1, Coul2, Coul3).

% Chaque habitant possède une nationalité différente (Italien, Norvégien ou Espagnol).
regle2() :-
    generate([maison(_, _, Nat1), maison(_, _, Nat2), maison(_, _, Nat3)]),
    dif3(Nat1, Nat2, Nat3).

%Indice 1 : L’Espagnol habite la maison directement à droite de la maison rouge.
indice1([maison(_, rouge,_), maison(_, _, espagnol), maison(_,_,_)]).
indice1([maison(_,_,_), maison(_,rouge,_), maison(_,_,espagnol)]).

%Indice 2 : Le Norvégien vit dans la maison bleue.
indice2([maison(_, bleu, norvegien), maison(_,_,_), maison(_,_,_)]).
indice2([maison(_,_,_), maison(_, bleu, norvegien), maison(_,_,_)]).
indice2([maison(_,_,_), maison(_,_,_), maison(_, bleu, norvegien)]).


%Indice 3 : L’Italien habite dans la maison n°2.
indice3([maison(_,_,_), maison(2,_,italien), maison(_,_,_)]).



test([M1,M2,M3]) :-
    regle0(),
    regle1(),
    regle2(),
    indice1([M1,M2,M3]),
    indice2([M1,M2,M3]),
    indice3([M1,M2,M3]).

solve([M1,M2,M3]) :-
    generate([M1,M2,M3]),
    test([M1,M2,M3]).