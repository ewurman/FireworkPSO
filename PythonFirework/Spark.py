import numpy as np
import utils
import random


CONSTRICTION_FACTOR = 0.7298;
TOWARD_PBEST = 2.05;
TOWARD_NBEST = 2.05;

class Spark:
# DO we need this class?

    def __init__(self, origin, velocity, Rocket):
        self.origin = origin
        self.velocity = velocity
        self.loc = np.array(origin)
        self.Rocket = Rocket
        self.pbest = np.array(origin)
        self.pbestVal = Rocket.pbestVal
        #self.lifespan = lifespan


    def localSearchUpdate(self, x, y, z):
        '''
        This is currently implemented as global PSO for a time step
        '''
        
        # position update
        print("HITHERE")
        np.add(self.loc, self.velocity)

        fitness = self.evaluate()

        x.append(self.loc[0])
        y.append(self.loc[1])
        z.append(fitness)

        print(x, y, z)

        if fitness < self.pbestVal:
            self.pbestVal = fitness
            self.pbest = np.array(self.loc)

        #now we want a velocity update
        dimensions = self.loc.size
        newVelocity = [0]*dimensions
        gbestLoc = self.Rocket.getRBestSparkLocation()
        for j in range(dimensions):
            r1 = random.uniform(0, TOWARD_PBEST)
            r2 = random.uniform(0, TOWARD_NBEST)
            newVelocity[j] = CONSTRICTION_FACTOR * (self.velocity[j] + r1*(self.pbest[j] - self.loc[j]) + r2*(gbestLoc[j] - self.loc[j]))

        self.velocity = np.array(newVelocity)

        return None



    def evaluate(self):
        if self.Rocket.evalFunc == utils.Function.Sphere:
            return self.evaluateSphere()

        elif self.Rocket.evalFunc == utils.Function.Ackley:
            return self.evaluateAckley()
            
        elif self.Rocket.evalFunc == utils.Function.Rosenbrock:
            return self.evaluateRosenbrock()

        elif self.Rocket.evalFunc == utils.Function.Rastrigin:
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