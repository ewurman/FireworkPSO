
import utils
import numpy as np
import math
import Spark

SPARK_LIFESPAN = 20

class Rocket:

    def __init__(self, ID, origin, velocity, evalFunc, numSparks):

        #want these to be np.array type
        self.id = ID
        self.loc = np.array(origin)
        self.origin = origin
        self.velocity = velocity
        self.pbest = np.array(origin)
        self.evalFunc = evalFunc
        self.numSparks = numSparks
        self.pbestVal = self.evaluate()
        self.sparks = []

        
    def printroc(self):
        print("id = {0} loc={1} vel={2} pbest={3}".format(self.id, self.loc, self.velocity, self.pbest))

    def launch(self, num_steps, x=[], y=[], z=[], returnValues = 0):
        self.pbestVal = self.evaluate()
        for i in range(num_steps):
            val = self.evaluate()
            if val > self.pbestVal:
                self.pbestVal = val
                self.pbest = np.array(self.loc)


            if self.loc.size == 2:
                x.append(self.loc[0])
                y.append(self.loc[1])
                z.append(val)

            self.loc = np.add(self.loc, self.velocity)


        # now we are at the end of launch
        self.explode()
        # Explode performs local search, we should now either update the rocket's pbest to getRBestSparkLocation() 
        #   and remove the sparks with self.sparks = []
        #  or 
        # We return the location and Swarm.py takes care of spawning new rockets at those rbests 
        if returnValues == 0:
            return self.getRBestSparkLocation()
        elif returnValues == 1:
            return self.getRBestSparkValue()
        else:
            return self.getRBestSparkLocationAndValue()


    def explode(self):
        #We want to spawn particles and have them do some sort of local search
        for i in range(self.numSparks):

            #create particle with random direction starting at pbest.
            v_min, v_max = utils.vel_min_max(self.evalFunc)

            ### TODO: talk to ian about starting velocitiies ####

            randomVelocity =  np.random.uniform(v_min, v_max, self.dimensions)
            spark = Spark(self.pbest, randomVelocity, self)
            #create particle with random direction starting at pbest.
            self.sparks.append(spark)

        for i in range(SPARK_LIFESPAN):
            for spark in self.sparks:
                spark.localSearchUpdate()

        return None


    def spawnNewRocket(self, new_velocity, new_origin, new_id):
        rocket = Rocket(new_id, new_origin, new_velocity, self.evalFunc, self.numSparks)
        return rocket



    def evaluate(self):
        if self.evalFunc == utils.Function.Sphere:
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

    def getRBestSparkLocation(self):
        rbestLoc = np.array(self.pbest)
        rbestVal = self.pbestVal
        for spark in self.sparks:
            if spark.pbestVal < rbestVal:
                rbestVal = spark.pbestVal
                rbestLoc = np.array(spark.pbest)
        return rbestLoc #np.array type


    def getRBestSparkValue(self):
        rbestVal = self.pbestVal
        for spark in self.sparks:
            if spark.pbestVal < rbestVal:
                rbestVal = spark.pbestVal
        return rbestVal #np.array type

    def getRBestSparkLocationAndValue(self):
        rbestLoc = np.array(self.pbest)
        rbestVal = self.pbestVal
        for spark in self.sparks:
            if spark.pbestVal < rbestVal:
                rbestVal = spark.pbestVal
                rbestLoc = np.array(spark.pbest)
        return (rbestLoc, rbestVal) #np.array type
