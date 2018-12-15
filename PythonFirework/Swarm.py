import tester
import utils
import plotter
import numpy as np
import Rocket
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Swarm(object):
    """docstring for Swarm"""
    def __init__(self, num_rockets, num_iterations, num_steps, algorithm, annealing, dimensions, numSparks, func):
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
            new_rocket = Rocket.Rocket(i, origin, velocity, self.func, self.dimensions, self.numSparks)
            self.rockets.append(new_rocket)

        for j in range(self.num_iterations):
            new_rockets = []
            for i in range(len(self.rockets)):

                rbestLoc = self.rockets[i].launch(self.steps, self.X, self.Y, self.Z)

                if i + 1 != self.num_rockets:
                    new_velocity = np.subtract(self.rockets[i+1].pbest, self.rockets[i].pbest) * (1.25 / self.steps) #reduce velocity step size
                else:
                    new_velocity = np.subtract(self.rockets[0].pbest, self.rockets[i].pbest)  * (1.25 / self.steps) #reduce velocity step size

                new_rocket = self.rockets[i].spawnNewRocket(new_velocity, rbestLoc, self.rockets[i].id)
                new_rockets.append(new_rocket)

            self.rockets = new_rockets


    def run_recursive(self, origin, iterations_left, total_iterations):
        ''' Has tendency to get stuck in local minimum. Thoughts on how to get out:
        - random chance to do explosion from spot on path,
        - Neighborhood PSO in local search instead
        - Increase the step number?
        - Decrease the spark number
        - random restart
        - Priority Queue for picking next with timing component?
        '''

        if iterations_left == 0:
            return
        print("Iteration", total_iterations - iterations_left + 1)

        if len(self.rockets) == 0:
            # first run through, build rockets
            for i in range(self.num_rockets):
                v_min, v_max = utils.vel_min_max(self.func)
                velocity = np.random.uniform(v_min, v_max, self.dimensions)
                new_rocket = Rocket.Rocket(i, origin, velocity, self.func, self.dimensions, self.numSparks)
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


        '''
        for triple in orderedRbest:
            print("rbestVal: ", triple[0], " at ", triple[1])
        '''


        #now we have them ordered, we want the best numRockets/spawn number
        numSpawn = 4
        mostPromising = orderedRbest[0:len(orderedRbest)//numSpawn]
        new_rockets = []
        next_id = 0
        for triple in mostPromising:
            rbestVal,rbestLoc,rocket = triple
            #print("Spawning from rbestVal: ", rbestVal, " at ", rbestLoc)
            for i in range(numSpawn):
                v_min, v_max = utils.vel_min_max(self.func)

                velocity = np.random.uniform(v_min, v_max, self.dimensions) * (iterations_left / total_iterations)
                new_rocket = rocket.spawnNewRocket(velocity, rbestLoc, next_id)
                new_rockets.append(new_rocket)
                next_id += 1

        self.rockets = new_rockets
        return self.run_recursive(origin, iterations_left - 1, total_iterations)

        





    def plot_history(self):
        plotter.plot_all_points(self.X, self.Y, self.Z)

    def plot_thing(self):
        tester.test(self.X, self.Y, self.Z)
