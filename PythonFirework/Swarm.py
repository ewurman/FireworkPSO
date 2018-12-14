
import utils
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
        self.explode = explodeParticles
        self.steps = num_steps
        self.plotref = plot
        self.X = []
        self.Y = []
        self.Z = []

    def run(self):
        if self.algorithm == 1:
            self.run_rotating()
        else:
            o_min, o_max = utils.loc_min_max(self.func)  ####### why algorithm and not evaluation function? ######
            origin = np.random.uniform(o_min, o_max, self.dimensions)
            self.run_recursive(origin, self.num_iterations)
        print("RUNNING")

        ##ORIGIN WORKING
        o_min, o_max = utils.loc_min_max(self.func)
        print("OMIN, OMAX = ", o_min, o_max)
        origin = np.random.uniform(o_min, o_max, self.dimensions)
        print("Origin = ", origin)
        
        if self.algorithm == 1:
            self.run_rotating(origin)
        else:
            self.run_recursive(origin, self.num_iterations)
            
        if self.dimensions == 2:    
            print(self.X)
            print(self.Y)
            print(self.Z)
            self.plot_and_anim()



    def run_rotating(self, origin):
        print("RUNNING ROTATING")
        for i in range(self.num_rockets):
            v_min, v_max = utils.vel_min_max(self.func)
            velocity = np.random.uniform(v_min, v_max, self.dimensions)
            new_rocket = Rocket.Rocket(i, origin, velocity, self.func, self.explode)
            new_rocket.printroc()
            thiss = input("Hold")
            self.rockets.append(new_rocket)


        for i in range(self.num_iterations):
            new_rockets = []
            for rocket in rockets:
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
        if iterations_left

        if len(rockets) == 0:
            # first run through
            for i in range(self.num_rockets):
                v_min, v_max = utils.vel_min_max(self.func)
                velocity = np.random.uniform(v_min, v_max, self.dimensions)
                new_rocket = Rocket(origin, velocity, self.func, self.explode)
                self.rockets.append(new_rocket)



        else:
        

        for i in range(self.num_iterations):
            for rocket in rockets:
                self.rockets[i].launch(self.steps)
                self.rockets[i].velocity = np.subtract(rockets[i+1].pbest, self.rockets[i].pbest) * 0.1 #reduce velocity step size
                self.rockets[i].origin = self.rockets[i].pbest






    def plot_and_anim(self):

        fig, ax = plt.subplots()
        xdata, ydata = [], []
        ln, = plt.plot([], [], 'ro', animated=True)

        def init():
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            return ln,

        def update(frame):
            xdata.append(self.X[frame])
            ydata.append(self.Y[frame])
            ln.set_data(xdata, ydata)
            return ln,

        ani = FuncAnimation(fig, update, frames=len(self.X),
                            init_func=init, blit=True)
        plt.show() 
