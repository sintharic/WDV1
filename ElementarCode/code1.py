import numpy as np

xMin = 0
xMax = 4*np.pi
N = 100000

def myFunction(x):
  # keine Klammern notwendig im return statement
  return np.sqrt(x)*np.sin(x)

dx = (xMax-xMin)/N
x = np.linspace(xMin, xMax, N+1)
# Gross- und Kleinschreibung wird unterschieden:
f = []
F = [] 

f.append(myFunction(xMin))
F.append(0)
print(x[0], f[0], F[0])

for i in range(N):
  j = i+1
  f.append(myFunction(x[j]))
  dF = dx*(f[i]+f[j])/2
  F.append(F[i]+dF)
  
  print(x[j], f[j], F[j])
