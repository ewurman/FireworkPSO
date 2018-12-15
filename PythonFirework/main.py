

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import Swarm
import Rocket
import utils



dims = 2
sparks = max(dims, 4)
swarm = Swarm.Swarm(num_rockets=16, num_iterations=500, num_steps=25, algorithm=2, annealing=0, dimensions=dims, numSparks=sparks, func=3)

swarm.run()
print("Swarm found a global best of ", swarm.gbest)

if dims == 2:
    swarm.plot_history()
