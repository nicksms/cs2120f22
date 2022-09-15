# Be sure you've done pip install z3-solver
from telnetlib import X3PAD
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
def hw2():
    
    
    
    
    # Create z3 variable(s) representing the unknown
    # Here, the unknown, x, is the square root of n.
    X, Y, Z = Bools('X Y Z')
    
    def helper(claim, veracity, name):
        s = Solver()
        if veracity:
            s.add(claim)
            if s.check() == unsat:
                print("[INCORRECT]: %s not valid, counterexample %s!" % (name, str(s.model())))
            else:
                print("[CORRECT]: %s valid!" % name)
        else:
            s.add(Not(claim))
            if s.check() == unsat:
                print("[INCORRECT]: %s is valid!" % name)
            else:
                print("[CORRECT]: %s not valid, counterexample %s!" % (name, str(s.model())))
    
    
    
    C = [None] * 21
    V = [None] * 21
    # 1. X ∨ Y, X ⊢ ¬Y 
    # As proposition in PL: ((X \/ Y) /\ X) -> ~Y
    C[1] = Implies(And(Or(X,Y),X),Not(Y))
    V[1] = False
    # IF we have X OR Y, and we have X,  we cannot have Y (false, consider when we have True or True)
    
    
    #2. X, Y ⊢ X ∧ Y              -- and introduction
    C[2] = Implies(And(X, Y), And(X,Y))
    V[2] = True
    # IF we have X and we have Y, we must have X AND Y (true)
    
    
    #3. X ∧ Y ⊢ X                 -- and elimination left
    C[3] = Implies(And(X, Y), X)
    V[3] = True
    # IF we have X AND Y, we must have X (true)
    
    
    #4. X ∧ Y ⊢ Y                 -- and elimination right
    C[4] = Implies(And(X, Y), Y)
    V[4] = True
    # IF we have X AND Y, we must have Y (true)
    
    
    #5. ¬¬X ⊢ X                   -- negation elimination
    C[5] = Implies(Not(Not(X)), X)
    V[5] = True
    # IF we have NOT NOT X, we must have X (true)
    
    
    #6. ¬(X ∧ ¬X)                 -- no contradiction
    C[6] = Not(And(X, Not(X)))
    V[6] = True
    # we cannot have X AND NOT X (true)
    
    
    #7. X ⊢ X ∨ Y                 -- or introduction left
    C[7] = Implies(X, Or(X, Y))
    V[7] = True
    # IF we have X then we must have X OR Y (true)
    
    
    #8. Y ⊢ X ∨ Y                 -- or introduction right
    C[8] = Implies(Y, Or(X, Y))
    V[8] = True
    # IF we have Y then we must have X OR Y (true)
    
    
    #9. X → Y, ¬X ⊢ ¬ Y           -- denying the antecedent
    C[9] = Implies(And(Implies(X, Y), Not(X)), Not(Y))
    V[9] = False
    # IF we have X IMPLIES Y and we have NOT X, we must have NOT Y (false, consider when we have "I am a fire breathing monster → I have too many classes on TuTh")
    
    
    #10. X → Y, Y → X ⊢ X ↔ Y      -- iff introduction
    C[10] = Implies(And(Implies(X, Y), Implies(Y, X)), X == Y)
    V[10] = True
    # IF we have X IMPLIES Y, and we have Y IMPLIES X, we must have X IFF Y (true)
    
    
    #11. X ↔ Y ⊢ X → Y            -- iff elimination left
    C[11] = Implies(X == Y, Implies(X, Y))
    V[11] = True
    # IF we have X IFF Y we must have X IMPLIES Y (true)
    
    
    #12. X ↔ Y ⊢ Y → X            -- iff elimination right
    C[12] = Implies(X == Y, Implies(Y,X))
    V[12] = True
    # IF we have X IFF Y we must have Y IMPLIES X (true)
    
    
    #13. X ∨ Y, X → Z, Y → Z ⊢ Z  -- or elimination
    C[13] = Implies(And(Or(X, Y), Implies(X, Z), Implies(Y, Z)), Z)
    V[13] = True
    # IF we have X OR Y and we have X IMPLIES Z and we have Y IMPLIES Z we must have Z (true)
    
    
    #14. X → Y, Y ⊢ X             -- affirming the conclusion
    C[14] = Implies(And(Implies(X, Y), Y), X)
    V[14] = False
    # IF we have X IMPLIES Y and we have Y we must have X (false, consider when we have "I am a fire breathing monster → I have too many classes on TuTh")
    
    
    #15. X → Y, X ⊢ Y             -- arrow elimination
    C[15] = Implies(And(Implies(X, Y), X), Y)
    V[15] = True
    # IF we have X IMPLIES Y and we have X we must have Y (true) (modus ponens :D)
    
    
    #16. X → Y, Y → Z ⊢ X → Z     -- transitivity of → 
    C[16] = Implies(And(Implies(X, Y), Implies(Y, Z)), Implies(X, Z))
    V[16] = True
    # IF we have X IMPLIES Y and we have Y IMPLIES Z we must have X IMPLIES Z (true)
    
    
    #17. X → Y ⊢ Y → X            -- converse
    C[17] = Implies(Implies(X, Y), Implies(Y, X))
    V[17] = False
    # IF we have X IMPLIES Y we must have Y IMPLIES X (false, consider "X = this shape is a square, Y = this shape is a rectangle" in general)
    
    
    #18. X → Y ⊢ ¬Y → ¬X          -- contrapositive
    C[18] = Implies(Implies(X, Y), Implies(Not(Y), Not(X)))
    V[18] = True
    # IF we have X IMPLIES Y we must have NOT Y IMPLIES NOT X (true)
    
    
    #19. ¬(X ∨ Y) ↔ ¬X ∧ ¬Y       -- DeMorgan #1 (¬ distributes over ∨)
    C[19] = Not(Or(X, Y)) == And(Not(X), Not(Y))
    V[19] = True
    # we have NOT (X OR Y) IFF we have (NOT X AND NOT Y) (true)
    
    
    #20. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y       -- Demorgan #2 (¬ distributes over ∧)
    C[20] = Not(And(X, Y)) == Or(Not(X), Not(Y))
    V[20] = True
    # we have NOT (X AND Y) IFF we have (NOT X OR NOT Y) (true)
    
    return [helper(C[i], V[i], "C%d" % i) for i in range(1, 21)]


hw2()