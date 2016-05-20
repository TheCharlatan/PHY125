from pylab import *
import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt

e = 0.976
a = 17.8

E = []
Mval = []
M = 0

curE = 0
step = 0.1

# Find some values for E to plot the orbit
while (M not in Mval and M < 2*math.pi and M >= 0):
  Mval.append(M)
  E.append(curE)
  curE = curE + step
  M = curE - e * math.sin(curE)

# Create lists for the coordinates to plot the orbit
x = []
y = []

for Eval in E:
  x.append(a * (math.cos(Eval)-e))
  y.append(a * (math.sqrt(1-math.pow(e, 2))*math.sin(Eval)))


print(x)
print(y)

fig = plt.figure()
sub = fig.add_subplot(111, autoscale_on=False, xlim=(-40,5), ylim=(-5,5))
sub.grid()

sun = sub.plot(0,0,'yo')
PLOT, = sub.plot([],[],'o', lw=2)
annotation = sub.annotate('Halley', xy=(x[0],y[0]))
annotation.set_animated(True)

interval = 0
def animate(i):
  x_val = x[i]
  y_val = y[i]
  annotation.xytext = (x_val, y_val)
  PLOT.set_data(x_val, y_val)
  return PLOT, annotation

def init():
  return PLOT, annotation

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)), init_func=init, interval = 25, blit=True)

sub.annotate('Sun', xy=(0,0), xytext=(-3,0))

plt.show()





