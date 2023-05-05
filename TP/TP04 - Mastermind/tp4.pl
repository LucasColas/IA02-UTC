nBienPlace(Code1, Code2, BP):-
    Code1 = [],
    Code2 = [],
    BP = 0.

nBienPlace(Code1, Code2, BP) :-
    [T1|R1] = Code1,
    [T2|R2] = Code2,
    T1 = T2,
    nBienPlace(R1, R2, BP2),
    BP is BP2+1.

nBienPlace(Code1, Code2, BP) :-
    [T1|R1] = Code1,
    [T2|R2] = Code2,
    dif(T1, T2),
    nBienPlace(R1, R2, BP2),
    BP is BP2.

longueur([],0).
   

longueur(L,N) :-
    [_|R1] = L,
    longueur(R1, N2),
    N is N2 + 1.


gagne(Code1, Code2) :- 
    longueur(Code1, L1),
    longueur(Code2, L2),
    nBienPlace(Code1, Code2, NB),
    NB =:= L1,
    NB =:= L2.

element(E,L) :-
    [T1|R1] = L,
    E = T1.

element(E,L) :-
    [_|R1] = L,
    element(E, R1).


enleve(_, L1, L2) :-
    L1 = [],
    L2 = [].

enleve(E, L1, L2) :-
    [T1|R1] = L1,
    E = T1,
    L2 = R1.

enleve(E, L1, L2) :-
    [T1|R1] = L1,
    dif(E, T1),
    enleve(E, R1, Ltmp),
    L2 = [T1|Ltmp].

% cas où les listes sont vides : on a fini
enleveBP([], [], [], []).

%tetes de listes égales: on enleve les têtes dans le résultat
enleveBP([T|R1], [T|R2], Code1Bis, Code2Bis) :-
	enleveBP(R1, R2, Code1Bis, Code2Bis).
% cas où les têtes de listes ne sont pas égales : on garde les têtes dans le résultat
enleveBP([T1|R1], [T2|R2], [T1|Tmp1], [T2|Tmp2]) :-
	T1 \= T2,
	enleveBP(R1, R2, Tmp1, Tmp2).

nMalPlacesAux(Code1, Code2, MP) :-
    Code1 = [],
    Code2 = [],
    MP = 0.

nMalPlacesAux(Code1, Code2, MP) :-
    [T1|R1] = Code1,
    [T2|R2] = Code2,
    T1 = T2,
    enleve(T1, R2, R2Bis),
    enleve(T1, R1, R1Bis),
    nMalPlacesAux(R1Bis, R2Bis, MP2),
    MP is MP2.

nMalPlacesAux(Code1, Code2, MP) :-
    [T1|R1] = Code1,
    [T2|R2] = Code2,
    dif(T1, T2),
    enleve(T1, R2, R2Bis),
    enleve(T1, R1, R1Bis),
    nMalPlacesAux(R1Bis, R2Bis, MP2),
    MP is MP2+1.

codeur(_, 0, []).
codeur(M, N, [Color | Ctmp]) :-
	N > 0,
	N2 is N-1,
	codeur(M, N2, Ctmp),
	random(0, M, Color).

