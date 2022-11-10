import numpy as np

xMin = 0
xMax = 4*np.pi
N = 100

def myFunction(x):
  return np.sqrt(x)*np.sin(x)

dx = (xMax-xMin)/N
x = np.linspace(xMin, xMax, N+1) # dieser Vektor ist N+1 lang

f = myFunction(x)
dF = (f[1:] + f[:-1])*dx/2 # Achtung: dieser Vektor ist N lang
F = np.zeros_like(f) # und dieser ist wieder N+1 lang
F[1:] = np.cumsum(dF)

np.savetxt('numpy.dat', np.column_stack((x,f,F)), fmt="%g")