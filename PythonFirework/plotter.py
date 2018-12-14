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

def plot_all_points(x,y,evals):

    def init():
        pathcol.set_offsets([[], []])
        ax.axis([0, 100, 0, 100])
        return [pathcol]

    def update(i, pathcol, y, particles):
        pathcol.set_offsets(particles[:i])
        pathcol.set_color(y[:i])
        return [pathcol]

    upperbound = max(evals)

    frames = len(x)
    particles = list(zip(x,y))

    # '#001dff' #blue
    # '#ff0000' #red
    c1='#1f77b4' #blue
    c2='#2ca02c' #green
    colors = []

    for val in evals:
        col = fadeColor(c1,c2,val/upperbound)
        colors.append(col)

    #x, y = np.array([]), np.array([])

    fig = plt.figure()
    xs, ys = zip(*particles)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    pathcol = plt.scatter([], [], c=[], s=5)

    anim = animation.FuncAnimation(
        fig, update, init_func=init, fargs=(pathcol, colors, particles), interval=500, frames=frames, 
        blit=True, repeat=False)
    plt.show()



# x = [0.0,1.,2.,3.,4.,5.,6.,7.,8.,9.]
# y = [0.0,1.,2.,3.,4.,5.,6.,7.,8.,9.]
# plot_all_points(x,y,y)