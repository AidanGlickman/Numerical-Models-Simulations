# Battle Sim!

## Scenario

You are a general in an army at the rise of cannons, and you want to create a mathematical model to figure out who will win a battle.

## Things

Nation A | Nation B
---- | ----
A: Number of A soldiers remaining | B: Number of B soldiers remaining
A<sub>k</sub>: A killability factor | B<sub>k</sub>: B killability factor


## Definitions

- Killability factor is the percentage of a kill each soldier can get. For example, a killability of 25% would mean that it takes 4 soldiers on one side to kill a soldier of the other side each time increment.

## Basic Scenario

Killability: 25%

Time | Nation A | Nation B
---- | ---- | ----
t=0 | 10000 | 10000
t=1 | 7500 | 7500
t=2 | 5625 | 5625
... | ... | ...

This scenario where everything is equal is boring, and no one will win. What if Nation A doubled their forces?

Killability: 25%

Time | Nation A | Nation B
---- | ---- | ----
t=0 | 20000 | 10000
t=1 | 17500 | 5000
t=2 | 1625 | 625
... | ... | ...

## Assumptions

- Assume all soldiers of each nation are equally effective
- There are no restorative effects to either side (No doctors)

## Relationships
