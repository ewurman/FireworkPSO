
import utils
import test2
import numpy as np
import Rocket
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Swarm(object):
    """docstring for Swarm"""
    def __init__(self, num_rockets, num_iterations, num_steps, algorithm, annealing, dimensions, numSparks, func, plot):
        super(Swarm, self).__init__()
        self.gbest = float("inf")
        self.num_rockets = num_rockets
        self.rockets = []
        self.num_iterations = num_iterations
        self.func = func
        self.algorithm = algorithm
        self.dimensions = dimensions
        self.numSparks = numSparks
        self.steps = num_steps
        self.plotref = plot
        self.X = []
        self.Y = []
        self.Z = []

    def run(self):

        o_min, o_max = utils.loc_min_max(self.func)
        origin = np.random.uniform(o_min, o_max, self.dimensions)

        if self.algorithm == 1:
            self.run_rotating(origin)
        else:

            self.run_recursive(origin, self.num_iterations, self.num_iterations)  



    def run_rotating(self, origin):
        for i in range(self.num_rockets):
            v_min, v_max = utils.vel_min_max(self.func)
            velocity = np.random.uniform(v_min, v_max, self.dimensions)
            new_rocket = Rocket.Rocket(i, origin, velocity, self.func, self.explode, self.numSparks)
            new_rocket.printroc()
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


    def run_recursive(self, origin, iterations_left, total_iterations):
        if iterations_left == 0:
            return

        if len(self.rockets) == 0:
            # first run through, build rockets
            for i in range(self.num_rockets):
                v_min, v_max = utils.vel_min_max(self.func)
                velocity = np.random.uniform(v_min, v_max, self.dimensions)
                new_rocket = Rocket.Rocket(i, origin, velocity, self.func, self.numSparks)
                self.rockets.append(new_rocket)
        # EndIf

        # Now we launch and record data
        rbestValLocs = []
        for rocket in self.rockets:
            rbestLoc, rbestVal = rocket.launch(self.steps, self.X, self.Y, self.Z, 2) # return loc and val with parameter of 2
            if rbestVal < self.gbest:
                self.gbest = rbestVal
            rbestValLocs.append((rbestVal, rbestLoc, rocket))
        orderedRbest = sorted(rbestValLocs, key=lambda x: x[0]) #sort from smallest to largest

        #now we have them ordered, we want the best numRockets/spawn number
        numSpawn = 4
        mostPromising = orderedRbest[0:len(orderedRbest)//numSpawn]
        new_rockets = []
        next_id = 0
        for triple in mostPromising:
            rbestVal,rbestLoc,rocket = triple
            for i in range(numSpawn):
                v_min, v_max = utils.vel_min_max(self.func)

                #TODO: lower v_min and max ranges to encourage convergence
                velocity = np.random.uniform(v_min, v_max, self.dimensions) * (iterations_left / total_iterations)
                new_rocket = rocket.spawnNewRocket(velocity, rbestLoc, next_id)
                new_rockets.append(new_rocket)
                next_id += 1

        self.rockets = new_rockets
        return self.run_recursive(origin, iterations_left - 1, total_iterations)

        






    def plot_history(self):
        test2.plot_all_points(self.X, self.Y, self.Z)
        
