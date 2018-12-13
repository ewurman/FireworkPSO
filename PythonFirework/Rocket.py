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
        self.evalFunc = evalFunc
        self.numParticles = explodeParticles
        self.pbestVal = self.evaluate()


    def launch(self, num_steps, x, y, z):
        self.pbestVal = self.evaluate()
        for i in range(num_steps):
            val = self.evaluate()
            if val > self.pbestVal:
                self.pbestVal = val
                self.pbest = np.array(loc)


            if self.loc.size == 2:
                x.append(self.loc[0])
                y.append(self.loc[1])
                z.append(val)
            np.add(self.loc, self.velocity)

        return None

    def explode(self):
        #We want to spawn particles and have them do some sort of local search
        for i in range(self.numParticles):
            return None
            #create particle with random direction starting at pbest.
            #TODO

    def evaluate(self):
        if self.evalFunc == utils.Function.Sphere:
            val = self.eva
            return self.evaluateSphere()

        elif self.evalFunc == utils.Function.Ackley:
            return self.evaluateAckley()
            
        elif self.evalFunc == utils.Function.Rosenbrock:
            return self.evaluateRosenbrock()

        elif self.evalFunc == utils.Function.Rastrigin:
            return self.evaluateRastrigin()


    def evaluateSphere(self):
        return np.sum(self.loc * self.loc) #???

    def evaluateAckley(self):
        firstSum = 0
        secondSum = 0
        dimensions = self.loc.size
        for i in range(dimensions):
            firstSum += self.loc[i]*self.loc[i];
            secondSum += math.cos(2 * math.pi * self.loc[i]);
    
        #-20.0 * exp(-0.2*sqrt(firstSum / (double)dimensions)) - exp(secondSum / (double) dimensions) + 20 + M_E;
        return -20.0 * math.exp(-0.2* math.sqrt(firstSum/dimensions)) - math.exp(secondSum / dimensions) + 20 + math.e

    def evaluateRosenbrock(self):
        total = 0
        dimensions = self.loc.size
        for i in range(dimensions - 1): #Why - 1
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
