

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import Swarm
import Rocket
import utils


Sphere = 1
Ackley = 2
Rosenbrock = 3
Rastrigin = 4

Rotating = 1
Recursive = 2

dims = 2
sparks = max(dims, 4)

swarm = Swarm.Swarm(num_rockets=4, num_iterations=5, num_steps=10, algorithm=Recursive, annealing=0, dimensions=dims, numSparks=3, func=Sphere)


swarm.run()
print("Swarm found a global best of ", swarm.gbest)

if dims == 2:
    swarm.plot_history()
