import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# test = np.random.uniform(0.0,1.0,(10,4))
# print(test)

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





T = 10
numbParticles = 2


x = [0.0,1.,2.,3.,4.,5.,6.,7.,8.,9.]
y = [0.0,1.,2.,3.,4.,5.,6.,7.,8.,9.]
particles = list(zip(x,y))

# '#001dff' #blue
# '#ff0000' #red

c1='#1f77b4' #blue
c2='#2ca02c' #green
colors = []

for z in y:
    print(z/10)
    col = fadeColor(c1,c2,z/10)
    print(col)
    colors.append(col)

print(particles)
thiss = input("sdohjf")
x, y = np.array([]), np.array([])


def init():
    pathcol.set_offsets([[], []])
    return [pathcol]

def update(i, pathcol, y, particles):
    pathcol.set_offsets(particles[:i])
    pathcol.set_color(y[:i])
    return [pathcol]

fig = plt.figure()
xs, ys = zip(*particles)
xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
pathcol = plt.scatter([], [], c=[], s=100)
plt.colorbar()

anim = animation.FuncAnimation(
    fig, update, init_func=init, fargs=(pathcol, colors, particles), interval=1000, frames=T, 
    blit=True, repeat=True)
plt.show()


