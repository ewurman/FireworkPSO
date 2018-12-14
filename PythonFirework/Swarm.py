
import utils
import test2
import numpy as np
import Rocket
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Swarm(object):
    """docstring for Swarm"""
    def __init__(self, num_rockets, num_iterations, num_steps, algorithm, annealing, dimensions, explodeParticles, func, plot):
        super(Swarm, self).__init__()
        self.gbest = float("inf")
        self.num_rockets = num_rockets
        self.rockets = []
        self.num_iterations = num_iterations
        self.func = func
        self.algorithm = algorithm
        self.dimensions = dimensions
        self.explode = explode
        self.steps = num_steps
        self.plotref = plot
        self.X = []
        self.Y = []
        self.Z = []

    def run(self):
        o_min, o_max = utils.loc_min_max(self.algorithm)  ####### why algorithm and not evaluation function? ######
        origin = np.random.uniform(o_min, o_max, self.dimensions)

        if self.algorithm == 1:
            self.run_rotating(origin)
        else:

            self.run_recursive(origin, self.num_iterations)  



    def run_rotating(self, origin):
        for i in range(self.num_rockets):
            v_min, v_max = utils.vel_min_max(self.algorithm)
            velocity = np.random.uniform(v_min, v_max, self.dimensions)
            new_rocket = Rocket.Rocket(i, origin, velocity, self.func, self.explode)
            self.rockets.append(new_rocket)


        for i in range(self.num_iterations):
            new_rockets = []
            for rocket in self.rockets:
                if i + 1 != self.num_iterations:
                    rbestLoc = rocket.launch(self.steps, self.X, self.Y, self.Z)
                    new_velocity = np.subtract(self.rockets[i+1].pbest, self.rockets[i].pbest) * (1.25 / self.steps) #reduce velocity step size
                    new_rocket = rocket.spawnNewRocket(new_velocity, rbestLoc, rocket.id)
                    new_rockets.append(new_rocket)

                else:
                    rbestLoc = rocket.launch(self.steps, self.X, self.Y, self.Z)
                    new_velocity = np.subtract(self.rockets[0].pbest, self.rockets[i].pbest)  * (1.25 / self.steps) #reduce velocity step size
                    new_rocket = rocket.spawnNewRocket(new_velocity, rbestLoc, rocket.id)
                    new_rockets.append(new_rocket)
            self.rockets = new_rockets


    def run_recursive(self, origin, iterations_left):

        for i in range(self.num_rockets):
            v_min, v_max = utils.vel_min_max(self.algorithm)
            velocity = np.random.uniform(v_min, v_max, self.dimensions)
            new_rocket = Rocket(origin, velocity, self.func, self.explode)
            self.rockets.append(new_rocket)

        ###### LOCAL SEARCH?? #######

        for i in range(self.num_iterations):
            self.rockets[i].launch(self.steps)
            self.rockets[i].velocity = np.subtract(rockets[i+1].pbest, self.rockets[i].pbest) * 0.1 #reduce velocity step size
            self.rockets[i].origin = self.rockets[i].pbest


    def plot_history(self):
        test2.plot_all_points(self.X, self.Y, self.Z)
        
