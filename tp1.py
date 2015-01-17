import numpy as np
import numpy.linalg as npla

#import des matrice

#fontion theta

def theta():

   t= np.loadtxt("data/t.txt")
   p= np.loadtxt("data/p.txt")

   N = t.size

   un= np.ones((1,N))

   x= np.vstack((t,un))

   theta= np.dot(np.linalg.inv(np.dot(x,x.T)), np.dot(x,p))

   return theta

print theta()
