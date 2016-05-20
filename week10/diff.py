from scipy.integrate import odeint

import numpy as np
import matplotlib.pyplot as pl

def euler(F, ini, t):
  delta_t = t[-1] - t[-2]
  values = []
  for time in t:
    ini = ini + F(ini, time) * delta_t
    values.append(1*ini)
  return values

def runge(F, ini, t):
  delta_t = t[-1] - t[-2]
  values = []
  for time in t:
    ini = ini + 1/2 * delta_t * (F(ini,time) + F(ini + delta_t * F(ini,time), time))
    values.append(1*ini)
  return values

def F(X,t):
  return np.array([X[2],X[3],0,-1])

ini = np.array([0,0,1,5])
t = np.linspace(0,10,30)
z = odeint(F,ini,t)
e = np.array(euler(F, ini, t))
r = np.array(runge(F, ini, t))

print(e)
print(z)
print(r)

#fig = pl.figure()

pl.subplot(3,1,1)
pl.scatter(z[:,0],z[:,1], color='orange')
pl.plot(t,t*(5-t/2))
#ax1.axes().set_aspect('equal')

pl.subplot(3,1,2)
pl.scatter(e[:,0],e[:,1], color='red')
pl.plot(t,t*(5-t/2))
#ax2.axes().set_aspect('equal')

pl.subplot(3,1,3)
pl.scatter(r[:,0],r[:,1], color='red')
pl.plot(t,t*(5-t/2))

pl.show()

