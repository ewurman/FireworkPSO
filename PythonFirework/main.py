

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import Swarm
import Rocket
import utils

swarm = Swarm.Swarm(num_rockets=4, num_iterations=5, num_steps=5, algorithm=1, annealing=0, dimensions=2, numSparks=5, func=2)
swarm.run()
swarm.plot_history()