from sympy import *

n = 4

# ys in the og paper
xs = x1,x2,x3,x4 = symbols("x_1 x_2 x_3 x_4")
ws = w1,w2,w3,w4 = symbols("w_1 w_2 w_3 w_4")

ws_in_xs = [2*x1 + 3*x2 + 4*x3 + 2*x4, x2 + 2*x3 + 2*x4, x2 + 2*x3, x2]

def psi(m):
  result = 0

  for j in range(n):
    for i in range(n):
      result += (ws[i]+ws[j])**m + (ws[i]-ws[j])**m

  return result

ms = [2,6,8,12]
ys = [simplify(expand(psi(m))) for m in ms]

def diff_y_by_x(i,j):
  # TODO fix the dependence on n=4
  # represents the ws as functions of the xs
  fs = [Function(f"f_{i+1}")(x1,x2,x3,x4) for i in range(n)]
  
  y = ys[i]
  for k in range(n):
    y = y.subs(ws[k], fs[k])

  dy = y.diff(xs[j])

  for k in range(n):
    for l in range(n):
      dy = dy.subs(fs[k].diff(xs[l]), ws_in_xs[k].diff(xs[l]))

  for k in range(n):
    dy = dy.subs(fs[k], ws[k])

  return dy


J = Matrix([[diff_y_by_x(i,j) for j in range(n)] for i in range(n)])

print("calculating J inverse...")

J_inv = J.adjugate()/J.det()

print("calculating As...")

# Using sympy derivative rules to apply derivation rules
def delta_expr_in_ws(i, expr):
  delta_i_xs = J_inv.col(i)
  delta_i_ws = ws_in_xs
  for j in range(n):
    for k in range(n):
      delta_i_ws[j] = delta_i_ws[j].subs(xs[k], delta_i_xs[k])

  fs = [Function('f_' + str(j)) for j in range(n)]
  t = symbols('t')
 
  result = expr
  for j in range(n):
    result = result.subs(ws[j], fs[j](t))

  result = result.diff(t)

  for j in range(n):
    result = result.subs(fs[j](t).diff(t), delta_i_ws[j]).subs(fs[j](t), ws[j])

  return result

A = [] 
for i in range(n):
  print(f"calculating A{i+1}...")

  delta_i_J = zeros(n)

  for j in range(n):
    for k in range(n):
      delta_i_J[j,k] = delta_expr_in_ws(i, J[j,k])

  A.append(delta_i_J * J_inv)
  print("Printing...")
  print(A[i])

