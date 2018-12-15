import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np


cat = [6.37672e+08,887886,1709.77,119.699,78.699,77.4274,76.9264,76.3262,76.018,75.8892,75.7397,32.5325,8.51632,7.97202,7.79471,7.48695,7.27724,6.95375,6.52678,6.25247,5.9682,5.65174,5.3317,4.98887,4.70279,4.4757,4.16161,3.9091,3.70057,3.51079,3.3017,3.04049,2.8334,2.63512,2.42228,2.13177,1.90632,1.61873,1.43816,1.27148,1.0977,0.984685,0.885564,0.744373,0.638951,0.538349,0.455172,0.387878,0.34044,0.309491,0.269015]
print(len(cat))

aas=input("asdf")

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
