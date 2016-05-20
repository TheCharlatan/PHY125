from scipy.integrate import odeint

import numpy as np
import matplotlib.pyplot as pl

omega = 1

def euler(F, ini, t):
  """Solves a differential equation with Euler's Method
  F: function to be solved for
  ini: array
      holds the starting requirements and is updated in every iteration
  t: linearly spaced array
      holds the time for the different points to be draw"""

  delta_t = t[-1] - t[-2]
  values = []
  for time in t:
    ini = ini + F(ini, time) * delta_t
    values.append(1*ini)
  return values


def runge_2(F, ini, t):
  """Solves a differential equation with Runge-Kutta 2
  F: function to be solved for
  ini: array
      holds the starting requirements and is updated in every iteration
  t: linearly spaced array
      holds the time for the different points to be draw"""

  delta_t = t[-1] - t[-2]
  values = []
  for time in t:
    ini = ini + 1/2 * delta_t * (F(ini,time) + F(ini + delta_t * F(ini,time), time))
    values.append(1*ini)
  return values


def F(X,t):
  """The differential function in a four dimensional vector, first two dimensions for space, latter for velocity into given spatial dimension"""

  return np.array([X[2],X[3],2*X[3],-2*X[2]+np.cos(omega * t)])


ini = np.array([0,0,0,0])
t = np.linspace(0,10,1000)

x = np.sin(2*t) + (2*np.sin(t * omega))/(omega*(4-omega**2))
y = 1/2 * ((2*np.cos(2*t)) + ((2*np.cos(t * omega))/(4-omega**2)))

z = odeint(F,ini,t)
e = np.array(euler(F, ini, t))
r = np.array(runge_2(F, ini, t))

#fig = pl.figure()

#pl.subplot(3,1,1, aspect='equal')
pl.scatter(z[:,0],z[:,1], color='orange', label='Odeint')
pl.scatter(e[:,0],e[:,1], color='green', label='Euler')
pl.scatter(r[:,0],r[:,1], color='blue', label='Runge2')
pl.plot(x,y, color='red', label='Exact')
pl.axis((-3,3,-3,3))
pl.axes().set_aspect('equal')
pl.legend()

#pl.subplot(3,1,2, aspect='equal')
#pl.scatter(e[:,0],e[:,1], color='green')
#pl.plot(x,y)
#pl.axis((-3,3,-3,3))
#pl.axes().set_aspect('equal')

#pl.subplot(3,1,3, aspect='equal')
#pl.scatter(r[:,0],r[:,1], color='blue')
#pl.plot(x,y)
#pl.axis((-3,3,-3,3))
#pl.axes().set_aspect('equal')

pl.show()

