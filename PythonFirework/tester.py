import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

evals = [0.0,1.,2.,3.,4.,5.,6.,7.,8.,9.]
upperbound = 10

def fadeColor(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    assert len(c1)==len(c2)
    assert mix>=0 and mix<=1, 'mix='+str(mix)
    rgb1=np.array([int(c1[ii:ii+2],16) for ii in range(1,len(c1),2)])
    rgb2=np.array([int(c2[ii:ii+2],16) for ii in range(1,len(c2),2)])   
    rgb=((1-mix)*rgb1+mix*rgb2).astype(int)
    #cOld='#'+''.join([hex(a)[2:] for a in rgb])
    #print(11,[hex(a)[2:].zfill(2) for a in rgb])
    c='#'+('{:}'*3).format(*[hex(a)[2:].zfill(2) for a in rgb])
    #print(rgb1, rgb2, rgb, cOld, c)
    return c



c1='#1f77b4' #blue
c2='#2ca02c' #green
colors = []

for val in evals:
    col = fadeColor(c1,c2,val/upperbound)
    colors.append(col)


print(len(colors))


switch = ['#DCDCDC'] * 5

colors = switch + colors[5:]

print(len(colors))




