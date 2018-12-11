import utils.py
import numpy as np

class Swarm(object):
	"""docstring for Swarm"""
	def __init__(self, num_rockets, num_iterations, algorithm, annealing, dimensions):
		super(Swarm, self).__init__()
		self.gbest = float("inf")
		self.rockets = [num_rockets]
		self.num_iterations = num_iterations
		self.func = func
		self.algorithm = algorithm
		self.dimensions = dimensions

	def run(self):
		if self.algorithm == 1:
			run_rotating()
		else
			run_recursive()

	def run_rotating(self):
		origin = np.random.uniform()
