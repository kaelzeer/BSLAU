import numpy as np

np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.2f}'.format})

nmax=70
eps=1E-8

'''
v=array[0..nmax]  of extended;
m=array[0..nmax,0..nmax]  of extended;
'''

def ch(x:float)->float:
	return 0.5*(np.exp(x) + np.exp(-x))

class alg:

	def __init__(self) -> None:
		self.x = np.zeros(nmax)
		self.f = np.zeros(nmax)
		self.y = np.zeros(nmax)
		self.y0 = np.zeros(nmax)
		self.b = np.zeros(nmax)
		self.A = np.zeros(nmax)

		self.c = np.zeros((nmax,nmax))
		self.c1 = np.zeros((nmax,nmax))

		self.n = 0
		self.b0 = 0.0


	def init(self):
		self.n = 10
		self.b0 = 1.5
		
		bj = 1
		ap = 0.0
		a = 1.0
		for j in range(nmax):
			self.b[j] = bj
			bj = bj*self.b0
			if j > 0:
				a *= (2*j-1)*(2*j)
			self.c[j,j]= a
			ap = a
			for p in range(1,nmax-j):
				ap *= (2*j+2*p-1)*(2*j+2*p)/((2*p-1)*(2*p))
				self.c[j,j+p] = ap
		for i in range(nmax):
			self.b[i] = self.b[i]/self.c[i,i]
			for j in range(i + 1): # necessary inclusive step
				self.c1[i,j] =self.c[j,i]/self.c[j,j]


	def _print(self, x : np.ndarray):
		print(f'n={self.n} b={self.b0}')
		for i in range(self.n):
			print(x[i])
		print('\n\n')


	def solve(self):
		zA = 0
		xs = 0.0
		r = 0.0

		self.A[0] = 1
		maxjp = 0
		for j in range(self.n):
			p = 0
			z = 1
			#repeat
			while True:
				if p>0:
					self.A[p] = 0
				zA = z
				for k in range(p): # necessary inclusive step
					zA = -zA
					self.A[p] += zA*self.c1[j+p,j+k]*self.A[k]
				xs = self.x[j]
				self.x[j] = xs+z*self.A[p]*self.b[j+p]
				r = abs(xs-self.x[j])
				p += 1
				z = -z
				if maxjp<j+p:
					maxjp=j+p

				#until
				if (r<eps) or (j+p>nmax):
					break
		print(f'j+p={maxjp}')


asd = alg()
asd.init()

# print(f'c:\n{asd.c}\n\n')

print(f'c:\n')
for i in range(10):
	for j in range(10):
		print(asd.c[i,j], end=' ')
	print()
print(f'c:\n')

print(f'c1:\n')
for i in range(10):
	for j in range(10):
		print(asd.c1[i,j], end=' ')
	print()
print(f'c1:\n')

asd.solve()
asd._print(asd.x)
r = 1.0
for i in range(asd.n):
	if i:
		r *= asd.b0/((2*i-1)*2*i)
	print(r/ch(np.sqrt(asd.b0)))


