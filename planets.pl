% Planet facts
planet(mercury).
planet(venus).
planet(earth).
planet(mars).
planet(jupiter).
planet(saturn).
planet(uranus).
planet(neptune).

% Distance from Sun
distance(mercury, closest).
distance(venus, second_closest).
distance(earth, third_closest).
distance(mars, fourth_closest).
distance(jupiter, fifth_closest).
distance(saturn, sixth_closest).
distance(uranus, seventh_closest).
distance(neptune, farthest).

% Planet type
type(mercury, terrestrial).
type(venus, terrestrial).
type(earth, terrestrial).
type(mars, terrestrial).

type(jupiter, gas_giant).
type(saturn, gas_giant).
type(uranus, ice_giant).
type(neptune, ice_giant).

% Rules
inner_planet(P) :-
    type(P, terrestrial).

outer_planet(P) :-
    type(P, gas_giant).

outer_planet(P) :-
    type(P, ice_giant).