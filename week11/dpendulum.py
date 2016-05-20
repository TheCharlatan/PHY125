from scipy.integrate import odeint

import numpy as np
import matplotlib.pyplot as pl
import matplotlib.animation as animation

class Pendulum:
  time = 0.0
  X = 0.0
  Y = 0.0
  x = 0.0
  y = 0.0
  b = 0.0
  l = 1.0
  omega = 0.0
  dt = 0.0
  e = 0.0
  q = np.array([0,0])
  u = 0
  g = 9.81

  def __init__(self, b=1, l=1, omega=1.0):
    self.X = 0
    self.Y = -b
    self.x = 0
    self.y = -(b+l)
    self.b = b
    self.l = l
    self.omega = omega
    self.dt = self.omega/50.0
    self.e = (self.b/self.l) * omega**2

  def step(self):
    self.time += self.dt
    self.X,self.Y = self.Motor()
    self.x,self.y = self.Free()

  def Motor(self):
    return self.b*np.sin(self.omega*self.time), -self.b*np.cos(omega*self.time)

  def Free(self):
    self.runge2()
    return self.X + self.l * np.sin(self.q[0]), self.Y + self.l * -np.cos(self.q[0])

  def runge2(self):
    """Solves a differential equation with Runge-Kutta 2
    F: function to be solved for
    ini: array
        holds the starting requirements and is updated in every iteration
    t: linearly spaced array
        holds the time for the different points to be draw"""

    #delta_t = t[-1] - t[-2]
    #values = []
    #for time in t:
    self.q = self.q + 1/2 * self.dt * (self.F(self.q,self.time) + self.F(self.q + self.dt * self.F(self.q,self.time), self.time+self.dt))


  def F(self,q,t):
    #"""The differential function in a four dimensional vector, first two dimensions for space, latter for velocity into given spatial dimension"""
    #return np.array([X[2],X[3],2*X[3],-2*X[2]+np.cos(omega * t)])
    return np.array([q[1], -np.sin(self.q[0]) - self.e * np.sin(self.q[0] - self.omega*t)])

#Angular frequency of the driving rod
omega = 2
#Length of the driving rod between its points of fixture and hinge with the free swinging point
b = 1
#Length of the flexible dysonant rod
l = 1
#Starting coordinates of the harmonic rod

pendel = Pendulum(b, l, omega)

fig = pl.figure()
ax = fig.add_subplot(111, xlim=(-(b+l),b+l), ylim=(-(b+l),b+l))
ax.grid()
Bpoint, = ax.plot([],[], 'r.')
Lpoint, = ax.plot([],[], 'b.')
Bline, = ax.plot([],[], 'k-')
Lline, = ax.plot([],[], 'k-')


def animate(i):
  pendel.step()
  Bpoint.set_data([pendel.X,pendel.Y])
  Bline.set_data([0,pendel.X],[0,pendel.Y])
  Lpoint.set_data([pendel.x,pendel.y])
  Lline.set_data([pendel.X,pendel.x],[pendel.Y,pendel.y])

ani = animation.FuncAnimation(fig, animate, interval=25)# init_func=init)

pl.show()

