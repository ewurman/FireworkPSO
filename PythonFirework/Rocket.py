import utils
import numpy as np
import math


class Rocket:

    def __init__(self, origin, velocity, evalFunc, explodeParticles):
        #want these to be np.array type
        self.loc = np.array(origin)
        self.origin = origin
        self.velocity = velocity
        self.pbest = np.array(origin)
        self.pbestVal = self.evaluate()
        self.evalFunc = evalFunc
        self.numParticles = explodeParticles

    def launch(self, num_steps):
        self.pbestVal = self.evaluate(evalFunc)
        for i in range(num_steps):
            val = self.evaluate()
            if val > self.pbestVal:
                self.pbestVal = val
                self.pbest = np.array(loc)
        return None

    def explode():
        #We want to spawn particles and have them do some sort of local search
        for i in range(self.numParticles):
            #create particle with random direction


    def evaluate(self):
        if self.evalFunc == Function.Sphere:
            return evaluateSphere()

        elif self.evalFunc == Function.Ackley:
            return evaluateAckley()
            
        elif self.evalFunc == Function.Rosenbrock:
            return evaluateRosenbrock()

        elif self.evalFunc == Function.Rastrigin:
            return evaluateRastrigin()


    def evaluateSphere(self):
        return np.sum(self.loc * self.loc)

    def evaluateAckley(self):
        firstSum = 0
        secondSum = 0
        dimensions = self.loc.size
        for i in range(dimensions):
            firstSum += self.loc[i]*self.loc[i];
            secondSum += cos(2 * math.pi * pos[i]);
    
        #-20.0 * exp(-0.2*sqrt(firstSum / (double)dimensions)) - exp(secondSum / (double) dimensions) + 20 + M_E;
        return -20.0 * math.exp(-0.2* math.sqrt(firstSum/dimensions)) - exp(secondSum / dimensions) + 20 + math.e

    def evaluateRosenbrock(self):
        total = 0
        dimensions = self.loc.size
        for i in range(dimensions - 1):
            #total += 100*(pos[i+1] - pos[i]*pos[i])*(pos[i+1] - pos[i]*pos[i]) + (pos[i] - 1)*(pos[i] - 1);
            total += 100*(self.loc[i+1] - self.loc[i]*self.loc[i])*(self.loc[i+1] - self.loc[i]*self.loc[i]) + (self.loc[i] - 1)*(self.loc[i] - 1)
        return total

    def evaluateRastrigin(self):        
        dimensions = self.loc.size
        fitness = 10 * dimensions
        for i in range(dimensions):
            #fitness += pos[i]*pos[i] - (10 * cos(2 * M_PI * pos[i]));
            fitness += self.loc[i]*self.loc[i] - (10 * math.cos(2 * math.pi * self.loc[i]))
        return fitness

