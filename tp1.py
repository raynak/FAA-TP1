import numpy as np
import numpy.linalg as npla

#import des matrice

t= np.loadtxt("data/t.txt")
p= np.loadtxt("data/p.txt")

N = t.size

un= np.ones((1,N))

x= np.array((t,un))

print x

theta= npla.inv(x*x.T) * (x*y)

print theta
