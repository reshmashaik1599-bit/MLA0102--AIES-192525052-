% Experiment 16 - Birds Fly Knowledge Base

bird(sparrow).
bird(pigeon).
bird(eagle).
bird(ostrich).
bird(penguin).

cannot_fly(ostrich).
cannot_fly(penguin).

can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).
