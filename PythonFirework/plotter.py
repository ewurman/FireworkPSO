import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from playsound import playsound

SOUND=False
Greyout=False
Export=True

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

def plot_all_points(x,y,evals,numsteps,rockets):

    def init():
        pathcol.set_offsets([[], []])
        ax.axis([-50, 50, -50, 50])
        plt.plot(x[0], y[0], color='green', marker='o')
        return [pathcol]

    def update(i, pathcol, col, particles):
        if SOUND and i % numsteps == 0 and i !=0:
            playsound('pop.mp3')
        if Greyout and i % (numsteps * rockets) == 0 and i !=0:
            hold = ['#DCDCDC'] * (i-1)
            col = hold + col[i-1:]




        pathcol.set_offsets(particles[:i])
        pathcol.set_color(col[:i])
        return [pathcol]

    upperbound = max(evals)

    frames = len(x)
    particles = list(zip(x,y))

    # '#001dff' #blue
    # '#ff0000' #red
    c1='#1f77b4' #blue
    c2='#ff0000' #red
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
        fig, update, init_func=init, fargs=(pathcol, colors, particles), interval=10, frames=frames, 
        blit=False, repeat=False)


    if Export:
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
        anim.save('Rot.mp4', writer=writer)

    plt.xlabel('x value')
    plt.ylabel('y value')
    plt.title('{} Fireworks Algorithm over {} iterations on Ackley Function'.format("Rotating", "10"))
    #plt.grid(True)
    #plt.show()    
    plt.show()


# x = [0.0,1.,2.,3.,4.,5.,6.,7.,8.,9.]
# y = [0.0,1.,2.,3.,4.,5.,6.,7.,8.,9.]
# plot_all_points(x,y,y)
