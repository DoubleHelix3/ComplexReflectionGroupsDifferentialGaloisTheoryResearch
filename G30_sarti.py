from random import random
from sympy import *

def S(subscript, ys):
  is_pairwise_distinct = lambda array: len(array) == len(set(array))
  
  tab = "  "

  code = "result = 0"
  for k in range(len(subscript)):
    code += "\n" + tab*k + f"for i{k} in range(4):"

  line = "\n" + tab * len(subscript)
  code += line + "indices = ["
  for k in range(len(subscript)):
    code += f"i{k}, "
  code += "]"
  
  code += line + "if is_pairwise_distinct(indices):"
  line += tab
  code += line + "result += 1"
  for k,s in enumerate(subscript):
    code += f" * (ys[i{k}]**{s})"

  ldict = {}
  exec(code, locals(), ldict)
  return ldict["result"]


def poly(xs):
  y0,y1,y2,y3 = ys = [x**2 for x in xs]
  fs =  2*S([5,1],ys) - 6*S([4,2],ys) - 12*S([4,1,1],ys) + 14*S([3,3],ys)
  fs += 9*S([3,2,1],ys) + 348*S([3,1,1,1],ys) + 30*S([2,2,2],ys) - 270*S([2,2,1,1],ys)

  fa =   y0**3 * (y1**2*y2 - y1*y2**2 + y2**2*y3 - y2*y3**2 + y3**2*y1 - y3*y1**2)
  fa += -y1**3 * (y2**2*y3 - y2*y3**2 + y3**2*y0 - y3*y0**2 + y0**2*y2 - y0*y2**2)
  fa +=  y2**3 * (y0**2*y1 - y0*y1**2 + y1**2*y3 - y1*y3**2 + y3**2*y0 - y3*y0**2)
  fa += -y3**3 * (y0**2*y1 - y0*y1**2 + y1**2*y2 - y1*y2**2 + y2**2*y0 - y2*y0**2)
  
  return fs + 33*sqrt(5)*fa

def poly_vec(x):
  return poly(x.transpose().tolist()[0])


tau = (1 + sqrt(5))/2

sigma1 = Matrix([[0,-1,0,0],[+1,0,0,0],[0,0,0,-1],[0,0,+1,0]])
sigma2 = Matrix([[0,0,-1,0],[0,0,0,+1],[+1,0,0,0],[0,-1,0,0]])
sigma3 = Matrix([[0,+1,0,0],[-1,0,0,0],[0,0,0,-1],[0,0,+1,0]])
sigma4 = Matrix([[0,0,+1,0],[0,0,0,+1],[-1,0,0,0],[0,-1,0,0]])

pi5 = (1/2) * Matrix([[tau, 0, 1-tau,-1],[0,tau,-1,tau-1],[tau-1,1,tau,0],[1,1-tau,0,tau]])
pi5_prime = (1/2) * Matrix([[tau,0,tau-1,1], [0,tau,-1,tau-1],[1-tau,1,tau,0],[-1,1-tau,0,tau]])

C = Matrix([[+1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]])

gens = [sigma1, sigma2, sigma3, sigma4, pi5, pi5_prime, C]

xs = x0,x1,x2,x3 = symbols("x0 x1 x2 x3")
#xs = [1,2,3,4]
#xs = [10*random(), 10*random(), 10*random(), 10*random()]

x_vec = Matrix(xs)

for gen in gens:
  pprint(simplify(poly_vec(gen * x_vec) - poly_vec(x_vec)) == 0)
  #pprint(((poly_vec(gen * x_vec) - poly_vec(x_vec))/poly_vec(x_vec)).evalf())

