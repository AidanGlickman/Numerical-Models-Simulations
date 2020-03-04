# Spiders Problem.

> The Spiders often wait in their webs or in trees than lower themselves silently on silk strands and leap onto prey passing beneath. **A single strand is strong enough to support the spider and one creture of the same size.**

## Problem Statement

How strong is said spider silk? (In terms of how many Empire State Buildings it could lift.)

## Information

* Spiders in the game reach a size of about 40ft across.
* Goliath Bird Eater Spider:
	* average legspan of 1 ft
	* 170 grams
* Therefore our multiplier is 40
* Giant boi weighs 10880 kg
* Spider silk is about 1.5 GPa

## Assumptions

* I will use the Goliath Bird Eater Spider as my real world counterpart, because they are quite similar in description of hunting method to the giant spiders.
	* I will use the female , as the art we found has egg sacs.
* I will assume that "40ft across" is referring to leg span. 
* We assume that the strength of spider silk is the same as the strength of kevlar, as that is pretty close to true.

## Procedure

* Found all our info for the Goliath Bird Eater.
* Square cube law: 170g * 40^3 = 10880 kg
* Plug strength of spider silk as s into s*a = f
* s*a = f -> snπr^2 = mg, where r is radius of spider silk, and m is the mass lifted, and n is number of strands
* the only thing changing in the circumstances of lifting another spider and lifting the empire state building is the number of strands and the mass lifted
* we find that n is proportional to to the mass, so n2/n1 = m2/m1, where variables subscripted with 1 are for the spider lifting circumstance and the other the eiffel tower lifting circumstance
* substitute n1=1 as the spider lifting scenario only has one strand, m2 with the mass of the Empire State Building (m2 = 331122430kg), and m1 with the mass of 2 giant spiders (m1=2*10880kg=21760kg)
* we know the Empire state building weighs 331122430kg from converting tons to kg from the esbnyc.com (The website of the empire state building)
* we solve for n2: n2/1 = 331122430kg/21760kg -> n2 = 15217.02344
* since the questions was how many strands are necessary and strands have to be natural numbers, we ceiling the number and get 15218 strands