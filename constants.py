
import scipy.integrate as integrate
from equations import *
from simpson import simpson
from numpy import *
import numpy as np
#Define constants that are used in project

#Neural network configuration paramaters
HIDDEN_NODES = 25
ALPHA = 2
LAYERS = 3
A = 0
#Tan-sigmoid function
def tansig(x):
  x = (x)
  eq = 2/(1+e**(-2*(x)))-1
  return eq

def sin(x):
  return sin(x)

#Linear function
def purelin(x):
    return x

#Leaku RELU
def lRelu(x):
  if x<0:
    return x/10
  else:
    return x  
def integration(x, Phi):
  #eq = integrate.quad(lambda t: Phi(x-t)*(t**(ALPHA-1)), 0, x-A)[0]/sqrt(pi) + integrate.quad(lambda t: h(x, t)*Phi(t), 0, 1)[0]
  # eq = integrate.quad(lambda t: Phi(x-t)*(t**(ALPHA-1)), 0, x-A)[0]*2/sqrt(pi)\
  #    + integrate.quad(lambda t: h(x, t)*Phi(t), 0, pi/2)[0]
  eq = integrate.quad(lambda t: Phi(x-t)*(t**(ALPHA-1)), 0, x-A)[0]\
    + integrate.quad(lambda t: h(x, t)*Phi(t), 0, pi/2)[0]
  return eq 

