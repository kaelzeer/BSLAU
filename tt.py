from math import perm
import numpy as np
np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.2f}'.format})

a = np.zeros((10,10))
c = np.zeros((10,10))
b = np.zeros((10,10))

for i in range(10):
	for j in range(i+1):
		c[i,j] = 1
print(c)
print('\n\n')

for j in range(10):
	for p in range(10-j):
		# a[j,j+p] += j * 1000 + p * 100
		n = 2 * j + 2 * p + 1
		k = 2 * j
		a[j,j+p] = perm(n,k)
		# print(f'j: {j}, p: {p}')
		# print(f'a: {a[j,j+p]}')
		# print(f'n: {n}, k: {k}')
		# print(f'perm: {perm(n,k)}')
print(a)
print('\n\n')

b = np.matmul(c,a)
print(b)
print('\n\n')
b = np.dot(c,a)
print(b)
