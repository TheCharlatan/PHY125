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
g = np.linspace(-1,1,N)
X,Y = np.meshgrid(g,g)

Z = X + 1j*Y
F = np.sin(Z).real

#F = 0*(X+Y)
#for i in range(0, len(F)):
#for j in range(0,len(F[i])):

last = 1*F
#L = 0*F

while (notconvergent(last, F)):
  last = 1*F
  L = 0*F
  #L[1:-1,1:-1] = F[1:-1,:-2] + F[1:-1,2:] + F[:-2,1:-1] + F[2:,1:-1] - 4*F[1:-1,1:-1]
  L[1:-1,1:-1] = (F[1:-1,:-2] + F[1:-1,2:] + F[:-2,1:-1] + F[2:,1:-1])/4
  F = 0*L
  F[1:-1,1:-1] = L[1:-1,1:-1]


lev = np.linspace(np.amin(F),np.amax(F),100)
pl.clabel(pl.contour(X,Y,F,levels=lev))
pl.axes().set_aspect('equal')
pl.show()




