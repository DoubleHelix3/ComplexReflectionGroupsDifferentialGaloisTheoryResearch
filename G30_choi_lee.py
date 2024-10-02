from random import random
from sympy import *

def plus_minus(v):
  result = []

  result.append(Matrix([0,+v[1],+v[2],+v[3]]))
  result.append(Matrix([0,+v[1],+v[2],-v[3]]))
  result.append(Matrix([0,+v[1],-v[2],+v[3]]))
  result.append(Matrix([0,+v[1],-v[2],-v[3]]))

  result.append(Matrix([0,-v[1],+v[2],+v[3]]))
  result.append(Matrix([0,-v[1],+v[2],-v[3]]))
  result.append(Matrix([0,-v[1],-v[2],+v[3]]))
  result.append(Matrix([0,-v[1],-v[2],-v[3]]))

  return result

tau = (1 + sqrt(5))/2

def poly(x_vec):
  E = [Matrix(v) for v in [[0,1,0,0], [0,-1,0,0], [0,0,1,0], [0,0,-1,0], [0,0,0,1], [0,0,0,-1]]]
  E += plus_minus([0,1/2,1/(2*tau),tau/2]) + plus_minus([0,1/(2*tau), tau/2, 1/2]) +  plus_minus([0,tau/2,1/2,1/(2*tau)])

  return prod([x_vec.dot(v) for v in E])



sigma1 = Matrix([[1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1]]).transpose()
sigma2 = Matrix([[1,0,0,0],[0,-1/(2*tau),-tau/2,1/2],[0,-tau/2,1/2,1/(2*tau)],[0,1/2,1/(2*tau),tau/2]]).transpose()
sigma3 = Matrix([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]]).transpose()
sigma4 = Matrix([[tau/2,0,1/(2*tau),1/2], [0,1,0,0], [1/(2*tau), 0, 1/2, -tau/2], [1/2, 0, -tau/2, -1/(2*tau)]]).transpose()

sigmas = [sigma1, sigma2, sigma3, sigma4]

xs = [100*random(), 100*random(), 100*random(), 100*random()] #symbols("x1 x2 x3 x4")

x_vec = Matrix(xs)

for sigma in sigmas:
  pprint(((poly(sigma * x_vec) - poly(x_vec))/poly(x_vec)).evalf())

