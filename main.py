from sympy import *
import random

n = 2
#a,b = symbols('a b', integer=True, positive=True) 
x1, x2 = x = symbols(f'x_1 x_2')

# invarients
p = [x1**2 + x2**2, x1**2 * x2**2]
#p = [sum([v**(a*b*i) for v in x]) for i in range(1, n)]
#p.append(prod(x)**a)

J = Matrix([[diff(p[i],x[j]) for j in range(n)] for i in range(n)])

'''
  x_eval = [i+1 for i in range(n)]
  J_eval = J
  for i,v in enumerate(x):
    J_eval = J_eval.subs(v,x_eval[i])

  conjecture = -((-1)**n)*factorial(n-1)*(a**n)*(b**(n-1))*prod(x)**(a-1)

  for i in range(n):
    for j in range(i+1,n):
      conjecture *= (x[j]**(a*b)-x[i]**(a*b))

  #pprint(conjecture**2)

  #J_eval_det = J_eval.det()
  #print(n, J_eval_det == conjecture)
'''

J_inv = J.inv()

# Using sympy derivative rules to apply derivation rules
def delta(i, expr):
  global n, x, J_inv
  delta_i_x = J_inv.col(i)

  f = [Function('f_' + str(j)) for j in range(n)]
  t = symbols('t')
 
  result = expr
  for j in range(n):
    result = result.subs(x[j], f[j](t))

  result = result.diff(t)

  for j in range(n):
    result = result.subs(f[j](t).diff(t), delta_i_x[j]).subs(f[j](t), x[j])

  return result

def delta_curried(i): 
  return lambda expr : delta(i, expr)

pprint(delta(1, x1))

#A = [J.applyfunc(delta_curried(i)) * J_inv for i in range(n)]

#pprint(factor(A[0][1,0]))
