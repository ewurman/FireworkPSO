

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import Swarm
import Rocket
import utils



dims = 8
swarm = Swarm.Swarm(num_rockets=32, num_iterations=50, num_steps=25, algorithm=2, annealing=0, dimensions=dims, numSparks=5, func=2)

swarm.run()
print("Swarm found a global best of ", swarm.gbest)

if dims == 2:
    swarm.plot_history()
