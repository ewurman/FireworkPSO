

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import Swarm
import Rocket
import utils


Sphere = 1
Ackley = 2
Rosenbrock = 3
Rastrigin = 4

functions = {
    1: 'Sphere',
    2: 'Ackley',
    3: 'Rosenbrock',
    4: 'Rastrigin'
}

Rotating = 1
Recursive = 2

algorithms = {
    1: 'Rotating',
    2: 'Recursive'
}

# iterations = 100
# sparks = 30
# sparklife = 10
# numrockets = 8
# steps = 10
# =248600

# iterations = 65
# sparks = 30
# sparklife = 10
# numrockets = 12
# steps = 10

# iterations = 50
# sparks = 30
# sparklife = 10
# numrockets = 16
# steps = 10
# =248600

dims = 30
sparks = max(dims, 4)

iterations = [100, 65, 50]
rockets = [8, 12, 16]

'''
with open("Results/FPSO_parameterTuning_Results.txt", 'w') as f:
    for func in [2,3,4]:
        for alg in [1,2]:
            for i in range(0,3): # which iterations and rocket number we are using
                f.write("# {0} FPSO on {1} with {2} rockets and {3} iterations \n".format(algorithms[alg], functions[func], rockets[i], iterations[i]))
                outputLine = ""
                for j in range(0,100): #try it 99 more times
                    swarm = Swarm.Swarm(num_rockets=rockets[i], num_iterations=iterations[i], num_steps=10, algorithm=alg, dimensions=dims, numSparks=sparks, func=func)                
                    swarm.run()
                    print("Completed trial {} for {} and {} with best of {}".format(j, functions[func], algorithms[alg], swarm.gbest))
                    outputLine += str(swarm.gbest) + ","
                f.write(outputLine[0:-1] + "\n") # take off last comma



'''
swarm = Swarm.Swarm(num_rockets=rockets[0], num_iterations=iterations[0], num_steps=10, algorithm=1, dimensions=dims, numSparks=sparks, func=2, benchmarks=2500)                
swarm.run()
print("gbest History: ", swarm.gbestEachBenchmark)

if dims == 2:
    swarm.plot_history()
#'''





