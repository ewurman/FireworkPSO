

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import Swarm
import Rocket
import utils

swarm = Swarm.Swarm(num_rockets=4, num_iterations=1, num_steps=5, algorithm=2, annealing=0, dimensions=2, numSparks=0, func=1, plot=1)
swarm.run()
swarm.plot_history()