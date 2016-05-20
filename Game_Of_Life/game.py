from pylab import *
from raster import Raster
import time
from matplotlib import animation
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot


#Spawn the grid with given visual dimensions:
x_dim = 70
y_dim = 70
spawn_probability = 10 #As in 1 in 4 cells spawn
limit = (x_dim*y_dim)/spawn_probability
quadrants = 4

ind = np.arange(quadrants)
width = 0.35


raster = Raster(x_dim, y_dim)
raster.random_spawn(spawn_probability)

#Block
raster.pop_form('Glider',2,2)
raster.pop_form('Toad',15,5)
raster.pop_form('Glider',10,10)
raster.pop_form('Toad', 24,24)
raster.pop_form('Glider', 30,5)
raster.pop_form('Glider', 40,60)


fig  = figure(facecolor='white')

#Add Axes to the figure
ax01 = fig.add_subplot(121, autoscale_on=True, label='Simulation') #Aspect='equal'
ax02 = fig.add_subplot(222, label='Population', xlim=(0,1000), ylim=(0,limit))
ax03 = fig.add_subplot(224, label='Histogram')

ax01.set_title('Simulation')
ax02.set_title('Population vs Rounds')
ax03.set_title('Histogram')

ax02.set_xlabel('Rounds')
ax02.set_ylabel('Population')
ax03.set_xlabel('Quadrants from 0 - 3')
ax03.set_ylabel('Population')


#Add data to the two subplots
im = ax01.imshow(raster.grid, cmap=plt.cm.binary, interpolation='none', extent=[0,x_dim,0,y_dim])
line, = ax02.plot([],[],lw=2) #line, returns an iterable of line, another syntax version would be: [line
bar_plot = ax03.bar([],[])


#Make sure no overlapping occurs
plt.tight_layout()

#Initial state of animation:
def init():
  im.set_data(raster.grid)
  line.set_data([],[])
  bar_plot = 0
  bar_plot = ax03.bar(ind, raster.live_quadrant, width)
  return bar_plot, im, line,

#Actual animation function
def animate(i):
  raster.run()
  im.set_data(raster.grid)
  line.set_data(raster.population_buffer, raster.round_alive)
  bar_plot = 0
  bar_plot = ax03.bar(ind, raster.live_quadrant, width)
  return bar_plot, im, line,

#Set the animation object, pass all the desired functions. Interval is ms between each fram
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=100,) #blit=True)

plt.show()


