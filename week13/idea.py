from __future__ import division
from numpy import linspace
from matplotlib.pyplot import figure, plot, show, axes, axis
from matplotlib.animation import FuncAnimation


def evolve(fx):
  ret = 0*fx
  ret[1:] = fx[:-1]
  ret[0] = fx[-1]
  return ret

def frame(_):
  global fx
  axes().clear()
  axis([-20,20,-0.5,1.5])
  fx = evolve(fx)
  plot(x,fx)


if __name__ == "__main__":
  x = linspace(-20,20,200)

  fx = 0*x
  fx[20:30] = 1

  fig = figure()
  anim  = FuncAnimation(fig, frame, range(1000))

  show()

