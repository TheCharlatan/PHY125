mport numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0,2*np.pi,100)

fig = plt.figure()
sub = fig.add_subplot(111, xlim=(x[0], x[-1]), ylim=(-1, 1))
PLOT, = sub.plot([],[])

def animate(i):
    PLOT.set_data(x[:i], np.sin(x[:i]))
    return PLOT,

ani = animation.FuncAnimation(fig, animate, frames=len(x), interval=10, blit=True)
plt.show()
