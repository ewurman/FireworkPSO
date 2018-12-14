# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# X = [1,2,3,4,5,6,7,8,9,0]
# Y = [1,2,3,4,5,6,7,8,9,0]
# Z = [.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0]


# fig, ax = plt.subplots()
# xdata, ydata, zdata = [], [], []
# scat, = plt.scatter(xdata, ydata, zdata)
# plt.set_cmap('hot')

# def init():
#     ax.set_xlim(-10, 10)
#     ax.set_ylim(-10, 10)
#     return ln,

# def update(frame):
#     xdata.append(X[frame])
#     ydata.append(Y[frame])
#     zdata.append(Z[frame])
#     ln.set_data(xdata, ydata)
#     scat.set_color(zdata)
#     return scat,

# ani = FuncAnimation(fig, update, init_func=init, blit=True)
# plt.show() 





import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def main():
    numframes = 100
    numpoints = 10
    color_data = np.random.random((numframes, numpoints))
    x = [1,2,3,4,5,6,7,8,9,0]
    y = [1,2,3,4,5,6,7,8,9,0]
    c = y

    xdata = []
    ydata = []
    colors = []

    fig = plt.figure()
    scat = plt.scatter(xdata, ydata, c=colors, s=100)

    ani = animation.FuncAnimation(fig, update_plot, frames=range(numframes),
                                  fargs=(color_data, scat))
    plt.show()

def update_plot(i, data, scat):
    
    scat.set_array()
    return scat,

main()









