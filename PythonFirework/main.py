

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

dims = 30
swarm = Swarm.Swarm(num_rockets=15, num_iterations=50, num_steps=10, algorithm=Rotating, annealing=0, dimensions=dims, numSparks=30, func=Ackley)

swarm.run()
print("Swarm found a global best of ", swarm.gbest)
print("NUM EVALS = " ,swarm.get_num_func_evals())
if dims == 2:
    swarm.plot_history()
