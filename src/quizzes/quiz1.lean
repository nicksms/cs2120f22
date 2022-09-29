/-
CS2120 Fall 2022 Sullivan. Quiz #1. Edit your answers into
this file using VSCode. Save the file to your *local* hard 
drive (File > Save As > local > ...). Submit it to the Quiz1
assignment on Collab.
-/

/-
#1: For each of the following questions give a yes/no answer 
and then a very brief explanation why that answer is correct.
To explain why your answer is correct, name the specific rule
of inference that tells you it's correct, or explain that 
there is no such valid inference rule.
-/

/-
#1A

If a ball, b, is round *and* b is also red, is b red?

A: yes/no: yes

B: Why? 
And elimination: round(b) AND red(B) |- red(B)

#1B

If flowers make you happy and chocolates make you happy,
and I give you flowers *or* I give you chocolates, will
you be happy?

A: yes/no: yes

B: Why?
or elimination: you give me flowers or you give me chocolate, flowers make me happy, chocolate makes me happy |- I will be happy


#1C: If giraffes are just zebras in disguise, then the 
moon is made of green cheese?

A. yes/: no?

B. Why? No rules seem to apply to this unless we assume some information about their veracity


#1D. If x = y implies that 0 = 1, then is it true that
x ≠ y?

A. yes/no: yes

B. Why? P → false |- ¬ P (proof by negation)



#1E. If every zebra has stripes and Zoe is a Zebra then
Zoe has stripes.

A. yes/no: yes

B. Why? arrow elimination: zebra(x) → stripes(x), zebra(zoe) |- stripes(zoe)


#1F. If Z could be *any* Zebra and Z has stripes, then 
*every* Zebra has stripes.

A. Yes/no: no

B: Why? information about one case does not let us conclude something about every case


#1G. If whenever the wind blows, the leaves move, and 
the leaves are moving, then the wind is blowing.

A. yes/no: no

B. Why? this is prop.14 from the hw, which we know is not necessarily true


#1H: If Gina is nice *or* Gina is tall, and Gina is nice,
then Gina is not tall. (The "or" here is understood to be
the or of predicate logic.)

A. yes/no: no

B. Why? this is prop.1 from the hw, which we know is not necessarily true
-/



/- 
#2

Consider the following formula/proposition in propositional
logic: X ∨ ¬Y.

#2A: Is is satisfiable? If so, give a model (a binding of 
the variables to values that makes the expressions true).
Yes: X:true, Y:false


#2B: Is it valid? Explain your answer. 
No, we can give a counterexample in X:false, Y:true

-/


/-
#3: 

Express the following propositions in predicate logic, by
filling in the blank after the #check command.

If P and Q are arbitrary (any) propositions, then if (P is 
true if and only if Q is true) then if P is true then Q is 
true.
-/

#check ∀ (P Q : Prop), (P↔Q) → (P → Q)



/-
#4 Translate the following expressions into English.
The #check commands are just Lean commands and can
be ignored here. 
-/


-- A
#check ∀ (n m : ℕ), n < m → m - n > 0

/-
Answer: for all n,m natural, n < m implies m-n > 0
-/

-- B

#check ∃ (n : ℕ), ∀ (m : nat), m >= n

/-
Answer: there exists some n such that for all m natural, m ≥ n
-/


-- C

variables (isEven: ℕ → Prop) (isOdd: ℕ → Prop)
#check ∀ (n : ℕ), isEven n ∨ isOdd n

/-
Answer: for all n natural, n is even or n is odd
-/


-- D

#check ∀ (P : Prop), P ∨ ¬P

/-
Answer: Every proposition is either true or not true
-/


-- E

#check ∀ (P : Prop), ¬(P ∧ ¬P)

/-
Answer: For every proposition P, we do not have that both P and not P
-/


/-
#5 Extra Credit

Next we define contagion as a proof of a slightly long
proposition. Everything before the comma introduces new
terms, which are then used after the comma to state the
main content of the proposition. 

Using the names we've given to the variables to infer
real-world meanings, state what the logic means in plain
natural English. Please don't just give a verbatim reading
of the formal logic. 
-/

variable contagion : 
  ∀ (Animal : Type) 
  (hasVirus : Animal → Prop) 
  (a1 a2 : Animal) 
  (hasVirus : Animal → Prop)
  (closeContact : Animal → Animal → Prop), 
  hasVirus a1 → closeContact a1 a2 → hasVirus a2

/-

This is a way of expressing the idea that if two animals come into close contact and one has a virus, the other will too.

-/
