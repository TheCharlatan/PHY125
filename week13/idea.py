from __future__ import division
from numpy import linspace, array
from matplotlib.pyplot import figure, plot, show, axes, axis
from matplotlib.animation import FuncAnimation
from pylab import *


def evolve(pop):
  ret = 0*pop
  for i in range(1, len(pop)-2):
    ret[i] = pop[i+1] + pop[i-1] - 2*pop[i] #- pop[i]**2 kill vampires on demand
  for i in range(len(pop)):
    ret[i] = ret[i] + pop[i]*(1-pop[i])
  return ret

def runge_2(F,pop,dt):
  pop = pop + dt * (1/2) * (F(pop) + F(pop+dt * F(pop)))
  return pop


def frame(_):
  global pop, dt
  pop = runge_2(evolve, pop, dt)
  plt.set_ydata(pop)


#Space in which the population is distributed
x = linspace(-20,20,200)
dt = 0.1

#Fraction of the population who have the idea at a point in space.
pop = 0*x
#Start with everybody over a certain spatial position have the idea
pop[20:30] = 1


fig = figure()

axes().clear()
axis([-20,20,-0.5,1.5])

plt, = plot(x,pop)
anim  = FuncAnimation(fig, frame, range(1000), interval=1)
show()

