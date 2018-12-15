import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

performance = [100,100,50,20,20,20,20,18,17,14]
numEvals = [100,200,300,400,500,600,700,800,900,1000]

performance2 = [130,130,30,10,10,8,8,1,0,0]
numEvals2 = [100,200,300,400,500,600,700,800,900,1000]

plt.plot(performance, numEvals)
plt.plot(performance2, numEvals2)

plt.xlabel('numEvals')
plt.ylabel('performance')
plt.title('{} Fireworks Algorithm vs {}'.format("Recursive", "Global PSO"))
plt.grid(True)
plt.show()