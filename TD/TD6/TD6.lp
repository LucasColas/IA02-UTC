% IA02 TD6
% NB : on peut mettre en simple quotes pour avoir les majuscules aux noms

homme(créon).
homme(hémon).
homme(œdipe).
homme(étéocle).
homme(ménécée).
homme(polynice).
homme(laïos).
homme(penthée).

femme(ismène).
femme(antigone).
femme(jocaste).
femme(eurydice). 

parent(penthée, ménécée).
parent(créon, hémon).
parent(eurydice, hémon).
parent(ménécée, jocaste).
parent(ménécée, créon).
parent(laïos, œdipe).
parent(jocaste, œdipe).
parent(œdipe, étéocle).
parent(œdipe, polynice).
parent(œdipe, antigone).
parent(œdipe, ismène).
parent(jocaste, étéocle).
parent(jocaste, polynice).
parent(jocaste, antigone).
parent(jocaste, ismène).

couple(œdipe,jocaste).
couple(jocaste,œdipe).
couple(laïos,jocaste).
couple(jocaste,laïos).



pere(X,Y) :- homme(X), parent(X,Y).
mere(X,Y) :- femme(X), parent(X,Y).

epoux(X,Y) :- couple(X,Y), homme(X).
epoux(X,Y) :- couple(Y,X), homme(X).

% epouse(X,Y) (X est l’épouse de Y)
epouse(X,Y) :- couple(X,Y), femme(X).
epouse(X,Y) :- couple(Y,X), femme(X).

%fils(X,Y) (X est le fils de Y)

fils(X,Y) :- homme(X),parent(Y,X).
fille(X,Y) :- femme(X),parent(Y,X).

enfant(X,Y):- parent(Y,X).

grandPere(X,Y):- pere(X,Z), parent(Z,Y).
grandMere(X,Y):- mere(X,Z), parent(Z,Y).

%grandParent(X,Y) (X est un grand parent de Y)
grandParent(X,Y):- grandPere(X,Y).
grandParent(X,Y):- grandMere(X,Y).

%petitFils(X,Y) (X est le petit-fils de Y)
petitFils(X,Y) :- grandParent(Y,X), homme(X).
petitFille(X,Y) :- grandParent(Y,X), femme(X).

memePere(X,Y):- pere(Z,X),pere(Z,Y),dif(X,Y).
memeMere(X,Y):- mere(Z,X),mere(Z,Y),dif(X,Y).
%(X a un parent en commun avec Y)
memeParent(X,Y):- memePere(X,Y).
memeParent(X,Y):- memeMere(X,Y).

%(X a les même parents que Y)
memeParents(X,Y):- memeMere(X,Y),memePere(X,Y).

frere(X,Y):- memeParents(X,Y), homme(X).
soeur(X,Y):- memeParents(X,Y), femme(X).

demiFrere(X,Y):-
    homme(X),
    memePere(X,Y),
    mere(Z,X),
    mere(T,Y),
    dif(Z,T).
demiFrere(X,Y):- 
    homme(X),
    memeMere(X,Y),
    pere(Z,X),
    pere(T,Y),
    dif(Z,T).
    

demiSoeur(X,Y):-
    femme(X),
    memePere(X,Y),
    mere(Z,X),
    mere(T,Y),
    dif(Z,T).
demiSoeur(X,Y):- 
    femme(X),
    memeMere(X,Y),
    pere(Z,X),
    pere(T,Y),
    dif(Z,T).

%oncle(X,Y) (X est l’oncle de Y)

oncle(X,Y) :-
    dif(X,Y),
    homme(X),
    parent(Z,Y), %Z parent du neuveu
	memeParent(X,Z).
	

tante(X,Y) :-
    dif(X,Y),
    femme(X),
    parent(Z,Y), %Z parent de la nice
	memeParent(X,Z).

% cousin(X,Y) %meme grand parents

% gendre(X,Y)
beauPere(X,Y):- 
    %mari de ta mere
    mere(Z,Y),
    pere(T,Y),
    couple(X,Z),
    dif(Z,Y).

beauPere(X,Y):-
    %pere de ma femme
    couple(Z,Y),
    pere(X,Z).

ascendant(X,Y):-
    parent(X,Y).

ascendant(X,Y):-
    parent(Z,Y),
    ascendant(X,Z).
%ascendant(X,ismène)


descendant(X,Y):-
    parent(Y,X).
descendant(X,Y):-
    parent(Y,Z),
    descendant(X,Z).
    
lignee(X,Y):-
    ascendant(X,Y).
lignee(X,Y):-
    ascendant(Y,X).

parente(penthée,X):-
     descendant(X,penthée)
parente(X,Y):-
    dif(X,Y),
    ascendant(Z,X),
    ascendant(Z,Y).

    
    
    
    
    
    
    
    
    
    
    
    
    