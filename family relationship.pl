% Experiment 15 - Family Knowledge Representation

male(john).
male(paul).
male(mike).

female(mary).
female(lisa).
female(susan).

parent(john, paul).
parent(john, mary).
parent(mary, lisa).
parent(mary, mike).
parent(paul, susan).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandchild(X, Y) :-
    grandparent(Y, X).
