#!/usr/bin/env python
# coding: utf-8

# In[15]:


## Stuff common to all our models
from fractions import Fraction
N = 10000
p = MixedIntegerLinearProgram()
v = p.new_variable()
# n = v["n"]
# p.add_constraint(n == N)
vars = tuple()
t = r0, X0, D0, Q0 = v["r0"], v["X0"], v["D0"], v["Q0"]
vars = vars + t
t = x2, x3, x4 = v["x2"], v["x3"], v["x4"] # xi = number of times we choose inner-degree i vertex
vars = vars + t
p.add_constraint(r0 == x2 + x3 + x4 + 1) # number of rounds, including final round
p.add_constraint(X0 == x2 + x3 + x4) # size of X_{r-1}
p.add_constraint(D0 >= 3 + 2*x2 + 3*x3 + 4*x4) # size of N_G[X_{r-1}]
p.add_constraint(Q0 <= 3 + x2 + 2*x3 + 3*x4) # size of N_G[X_{r-1}]

t = r, X, D, L, Q, K, n = v["r"], v["X"], v["D"], v["L"], v["Q"], v["K"], v["n"]
vars = vars + t

p.add_constraint(n == N)  # number of vertices in G
for x in vars:
    p.add_constraint(x >= 0)


## Analysis of BestGreedy

x23u = v["x23u"]  # number of times we do 2-3 combo
p.add_constraint(x23u >= 0)
R = v["R"] # size of B(G_{r-1}-B(G_{r-1})) 
p.add_constraint(R >= 0)
S = v["S"] # isolated vertices after peeling two layers off of $G_{r-1}
p.add_constraint(S >= 0)

p.add_constraint(x2 == 0) # We never take an inner-degree 2 vertex by itself
p.add_constraint(r == r0 + x23u) # number of rounds, including final round
p.add_constraint(D >= D0 + 5*x23u) # each 2-3 move creates 5 new dominated vertices
p.add_constraint(Q <= Q0 + 2*x23u) # each 2-3 move increases boundary size by at most 2
p.add_constraint(R <= Q)  # because G_{r-1} is 2-critical
p.add_constraint(L >= x23u) # each 2-3 move isolates v_1
p.add_constraint(X == X0 + 2*x23u) # size of X_{r-1}
p.add_constraint(D == X + L + Q)
p.add_constraint(D + R + S == n) # By definition
p.add_constraint(K <= 2*R/3 + S/3) # Size of set we need to finish G_{r-1} (can we do better here?)
p.set_objective(X + K) # Size of the final set X_r
ds = p.solve()
f = Fraction(ds/N).limit_denominator(int(100))
print("n = {}, sol = {}n ~ ({})n".format(N, ds/N, f))
sol = p.get_values(v)
print(sol)


# In[56]:


## Stuff common to all our models
from fractions import Fraction
N = 10000
p = MixedIntegerLinearProgram()
v = p.new_variable()
# n = v["n"]
# p.add_constraint(n == N)
vars = tuple()
t = r0, X0, D0, Q0 = v["r0"], v["X0"], v["D0"], v["Q0"]
vars = vars + (L,)
t = x2, x3, x4 = v["x2"], v["x3"], v["x4"] # xi = number of times we choose inner-degree i vertex
vars = vars + (L,)
L = v["L"]  
vars = vars + (L,)
p.add_constraint(r0 == x2 + x3 + x4 + 1) # number of rounds, including final round
p.add_constraint(X0 == x2 + x3 + x4) # size of X_{r-1}
p.add_constraint(D0 >= 3 + 2*x2 + 3*x3 + 4*x4) # size of N_G[X_{r-1}]
p.add_constraint(Q0 <= 3 + x2 + 2*x3 + 3*x4) # size of N_G[X_{r-1}]

vars2 = r, X, D, L, Q, K, n = v["r"], v["X"], v["D"], v["L"], v["Q"], v["K"], v["n"]
p.add_constraint(n == N)  # number of vertices in G

vars = vars0 + vars1 + vars2

for x in vars:
    p.add_constraint(x >= 0)


## Analysis of SimpleGreedy

S = v["S"] # isolated vertices after peeling outer layer off of $G_{r-1}
p.add_constraint(S >= 0)

print(vars)
p.add_constraint(r == r0) 
p.add_constraint(D == D0) 
p.add_constraint(Q == Q0) 
p.add_constraint(Q >= 3*S)  # Because each isolated vertex is surrounded
p.add_constraint(X == X0) 
p.add_constraint(D == X + L + Q)
p.add_constraint(D + S == n) # By definition
p.add_constraint(K <= S) # Size of set we need to finish G_{r-1} 
p.set_objective(X + K) # Size of the final set X_r
ds = p.solve()
f = Fraction(ds/N).limit_denominator(int(100))
print("n = {}, sol = {}n ~ ({})n".format(N, ds/N, f))
sol = p.get_values(v)
print(sol)


# In[68]:


## Stuff common to all our models
from fractions import Fraction
N = 10000
p = MixedIntegerLinearProgram()
v = p.new_variable()
# n = v["n"]
# p.add_constraint(n == N)
vars = tuple()
t = r0, X0, D0, Q0 = v["r0"], v["X0"], v["D0"], v["Q0"]
vars = vars + (L,)
t = x2, x3, x4 = v["x2"], v["x3"], v["x4"] # xi = number of times we choose inner-degree i vertex
vars = vars + (L,)
L = v["L"]  
vars = vars + (L,)
p.add_constraint(r0 == x2 + x3 + x4 + 1) # number of rounds, including final round
p.add_constraint(X0 == x2 + x3 + x4) # size of X_{r-1}
p.add_constraint(D0 >= 3 + 2*x2 + 3*x3 + 4*x4) # size of N_G[X_{r-1}]
p.add_constraint(Q0 <= 3 + x2 + 2*x3 + 3*x4) # size of N_G[X_{r-1}]

vars2 = r, X, D, L, Q, K, n = v["r"], v["X"], v["D"], v["L"], v["Q"], v["K"], v["n"]
p.add_constraint(n == N)  # number of vertices in G

vars = vars0 + vars1 + vars2

for x in vars:
    p.add_constraint(x >= 0)


## Analysis of BetterGreedy

x21u = v["x21u"]  # number of times we do 2-1 combo
p.add_constraint(x23u >= 0)
S = v["S"] # isolated vertices after peeling outer layer off of $G_{r-1}

print(vars)
# p.add_constraint(x2 == 0) # We never take an inner-degree 2 vertex by itself
p.add_constraint(r == r0 + x21u) # number of rounds, including final round
p.add_constraint(D >= D0 + 2*x21u) # each 2-3 move creates 5 new dominated vertices
p.add_constraint(Q <= Q0) # each 2-1 moves don't increases boundary size
p.add_constraint(L >= x21u) # each 2-1 move isolates v_1
p.add_constraint(x2 <= x21u + 1)  # Never take two inner-degree-2 vertices in a row
p.add_constraint(Q >= 3*S)  # Because each isolated vertex is surrounded
p.add_constraint(X == X0 + x21u) # size of X_{r-1}
p.add_constraint(D == X + L + Q)
p.add_constraint(D + S == n) # By definition
p.add_constraint(K <= S) # Size of set we need to finish G_{r-1} (can we do better here?)
p.set_objective(X + K) # Size of the final set X_r
ds = p.solve()
f = Fraction(ds/N).limit_denominator(int(100))
print("n = {}, sol = {}n ~ ({})n".format(N, ds/N, f))
sol = p.get_values(v)
print(sol)

