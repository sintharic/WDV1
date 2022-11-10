import numpy as np

a = np.array( (1,1,1) )
# alternativ: a = np.ones(3)
b = np.array( (-1,0,1) )
# alternativ: b = np.linspace(-1,1,3)

print('\n')
print('{} + {} = {}\n'.format(a, b, a+b))
print('{} - {} = {}\n'.format(a, b, a-b))
print('{} * {} = {}\n'.format(a, b, a*b))
print('{} x {} = {}, Kreuzprodukt\n'.format(a, b, np.cross(a, b)))
print('{} . {} = {}, Skalarprodkt\n'.format(a, b, np.dot(a, b)))

identMat = np.identity(3)
print(identMat,'\n')

matrix = np.full((2,6),0)
# alternativ: matrix = np.zeros((2,6))
print(matrix,'\n')
