from sympy import *

gens = [ [[1,0], [0,-1]] ]
n = len(gens[0])

def y_vec(x_vec):
  x1,x2, = x_vec
  return x1**2 + x2**2


xs = [Symbol("x"+str(i)) for i in range(1,n+1)]
x_vec = Matrix(xs)

for gen in gens:
  gen = Matrix(gen)
  r = y_vec(gen * x_vec) - y_vec(x_vec)
  pprint(simplify(r))

