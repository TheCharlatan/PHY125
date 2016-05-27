import numpy as np
import math as math
import matplotlib.pyplot as pl


def notconvergent(last, current):
  for i in range(0, len(last)):
    for j in range(0, len(last[i])):
      delta = math.fabs(last[i][j] - current[i][j])
      if delta > 0:
        return False
  return True

N = 51
K = int(N/2)+1
g = np.linspace(-1,1,N)
X,Y = np.meshgrid(g,g)

F = 0*(X+Y)

#Code to set the Resistor grid
Q = 1*F[1:-1, 1:-1]
for i in range(1, len(F) - 2):
  for j in range(1,len(F[i]) - 2):
    if i == K+2 and j== K + 1:
      Q[i][j] = (F[i+1][j] + F[i-1][j] + F[i][j+1] + F[i][j-1]-1)/4
    elif i == j == K:
      Q[i][j] = (F[i+1][j] + F[i-1][j] + F[i][j+1] + F[i][j-1]+1)/4
F[1:-1, 1:-1] = Q


last = 1*F
L = 0*F

while (notconvergent(last, F)):
  last = 1*F
  L = 0*F
  #L[1:-1,1:-1] = F[1:-1,:-2] + F[1:-1,2:] + F[:-2,1:-1] + F[2:,1:-1] - 4*F[1:-1,1:-1]
  L[1:-1,1:-1] = (F[1:-1,:-2] + F[1:-1,2:] + F[:-2,1:-1] + F[2:,1:-1])/4
  F = 0*L
  F[1:-1,1:-1] = L[1:-1,1:-1]

print(F[K:K+5, K:K+4])

lev = np.linspace(np.amin(F),np.amax(F),11)
pl.clabel(pl.contour(X,Y,F,levels=lev))
pl.axes().set_aspect('equal')
pl.show()




