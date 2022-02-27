from numpy import *
import numpy as np
import scipy.integrate as integrate
#Define equations of the examples in the project file

NUMBER = 2 #No. of examples in project

#Right-side equation
def right_eq(x):
    #eq = 2*sqrt(x-1)/sqrt(pi)+np.e**x + 1/2
    # eq = 4*((x-1)**(3/2))*(2*x+3)/(15*sqrt(pi))\
    #     +(pi**2)*x/8+1
    # eq = 2*x - sin(x) +1
    eq = (x-(np.e**x)*cos(x)-np.e**(pi/2))/2
    return eq
#Analytical solution
def analytic(x):
    #eq = 1
    # eq = x
    # eq = sin(x)
    eq = (np.e**x)*sin(x)
    return eq

def h(x, t):
    #eq = np.e**x+t
    # eq = sin(t) + x
    # eq = x + t
    eq = -1
    return eq
