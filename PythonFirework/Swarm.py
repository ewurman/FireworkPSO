import utils
import numpy as np
import Rocket


class Swarm(object):
    """docstring for Swarm"""
    def __init__(self, num_rockets, num_iterations, num_steps, algorithm, annealing, dimensions, explodeParticles, plot, func):
        super(Swarm, self).__init__()
        self.gbest = float("inf")
        self.num_rockets = num_rockets
        self.rockets = []
        self.num_iterations = num_iterations
        self.func = func
        self.algorithm = algorithm
        self.dimensions = dimensions
        self.explode = explodeParticles
        self.steps = num_steps
        self.plotref = plot

    def run(self):
        if self.algorithm == 1:
            self.run_rotating()
        else:
            o_min, o_max = utils.loc_min_max(self.algorithm)  ####### why algorithm and not evaluation function? ######
            origin = np.random.uniform(o_min, o_max, self.dimensions)
            self.run_recursive(origin, self.num_iterations)

    def run_rotating(self):
        o_min, o_max = utils.loc_min_max(self.algorithm)
        origin = np.random.uniform(o_min, o_max, self.dimensions)

        for i in range(self.num_rockets):
            v_min, v_max = utils.vel_min_max(self.algorithm)
            velocity = np.random.uniform(v_min, v_max, self.dimensions)
            new_rocket = Rocket.Rocket(origin, velocity, self.func, self.explode)
            self.rockets.append(new_rocket)

        ###### LOCAL SEARCH?? #######

        for i in range(self.num_iterations):
            if i + 1 != self.num_iterations:
                self.rockets[i].launch(self.steps)
                self.rockets[i].velocity = np.subtract(self.rockets[i+1].pbest, self.rockets[i].pbest) * 0.1 #reduce velocity step size
                self.rockets[i].origin = self.rockets[i].pbest  

                ### Not sure this is the best way to respawn rockets ###

            else:
                self.rockets[i].launch(self.steps)
                self.rockets[i].velocity = np.subtract(self.rockets[0].pbest, self.rockets[i].pbest) * 0.1 #reduce velocity step size
                self.rockets[i].origin = self.rockets[i].pbest



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



