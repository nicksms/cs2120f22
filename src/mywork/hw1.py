# name  :   Nicholas Winschel
# id    :   pvz6tx

from re import A
from z3 import Bool, And, Or, Not, Solver
from itertools import combinations


def at_most_one(literals):
    c = []
    for pair in combinations(literals, 2):
        a, b = pair[0], pair[1] #can't I just do a,b = pair?
        c += [Or(Not(a), Not(b))]
    return And(c)

x = [[Bool("x_%i_%i" % (i,j)) for j in range(5)] for i in range(5)]

s = Solver()

for i in range(5):
    s.add(Or(x[i]))

for i in range(5):
    col = []
    for j in range(5):
        col += [x[j][i]]
    s.add(at_most_one(col))
    s.add(at_most_one(x[i]))

for i in range(4):
    diag_1 = []
    diag_2 = []
    diag_3 = []
    diag_4 = []
    for j in range(5-i):
        diag_1 += [x[i+j][j]]
        diag_2 += [x[i+j][4-j]]
        diag_3 += [x[4-(i+j)][j]]
        diag_4 += [x[4-(i+j)][4-j]]
    s.add(at_most_one(diag_1))
    s.add(at_most_one(diag_2))
    s.add(at_most_one(diag_3))
    s.add(at_most_one(diag_4))

print(s.check())
m = s.model()

print("\n".join([" ".join([("x" if m.evaluate(x[i][j]) else ".") for j in range(5)]) for i in range(5)]))