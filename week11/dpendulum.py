from scipy.integrate import odeint

import numpy as np
import matplotlib.pyplot as pl
import matplotlib.animation as animation

#Angular frequency of the driving rod
omega = 1
#Length of the driving rod between its points of fixture and hinge with the free swinging point
b = 1

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


def Motor(b,omega,t):
  return b*np.sin(omega*t), -b*cos(omega*t)

def run()

#Starting position
X = 0
Y = b

fig = pl.figure()
ax = fig.add_subplot(111, autoscale_on=False)
ax.grid()
point, = ax.plot([],[], 'r.')

def init():
  point.set_data([x],[y])
  return point

def animate(i):
  X,Y = run()
  point.set_data(x,y)
  return point

ani = animation.FuncAnimation(fig, animate, interval=25, blit=True, init_func=init)



