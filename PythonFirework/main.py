

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import Swarm
import Rocket
import utils

## https://matplotlib.org/users/colormapnorms.html color normalization for plotting
## https://matplotlib.org/api/pyplot_summary.html color map stuff

## https://brushingupscience.com/2016/06/21/matplotlib-animations-the-easy-way/ good stuff for animations
"""
o_min, o_max = utils.loc_min_max(1)
origin = np.random.uniform(o_min, o_max, 2)
v_min, v_max = utils.vel_min_max(1)
velocity = np.random.uniform(v_min, v_max, 2)
rocket = Rocket.Rocket(origin, velocity, 1, 1)
"""

"""
create lists that we will pass through to eval, eval will update those lists with append https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
then update will just pull the ith datapoint in using xdata.append(i)

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated=True)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show() 


"""
#(self, num_rockets, num_iterations, num_steps, algorithm, annealing, dimensions, explodeParticles, plot)

swarm = Swarm.Swarm(num_rockets=4, num_iterations=1, num_steps=5, algorithm=1, annealing=0, dimensions=2, explodeParticles=0, func=1, plot=1)
swarm.run()