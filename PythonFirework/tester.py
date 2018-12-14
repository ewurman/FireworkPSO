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

xyc = range(20)

print(xyc)

plt.subplot(121)
plt.scatter(xyc[:13], xyc[:13], c=xyc[:13], s=35, vmin=0, vmax=20)
plt.colorbar()
plt.xlim(0, 20)
plt.ylim(0, 20)

plt.subplot(122)
plt.scatter(xyc[8:20], xyc[8:20], c=xyc[8:20], s=35, vmin=0, vmax=20)   
plt.colorbar()
plt.xlim(0, 20)
plt.ylim(0, 20)

plt.show()




import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Create rain data
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('growth',   float, 1),
                                      ('color',    float, 4)])

# Initialize the raindrops in random positions and with
# random growth rates.
rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)

# Construct the scatter which we will update during animation
# as the raindrops develop.
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')


def update(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n_drops

    # Make all colors more transparent as time progresses.
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)
    print(len(rain_drops['color']))

    # Make all circles bigger.
    rain_drops['size'] += rain_drops['growth']

    # Pick a new position for oldest rain drop, resetting its size,
    # color and growth factor.
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (0, 0, 0, 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])


# Construct the animation, using the update function as the animation
# director.
animation = FuncAnimation(fig, update, interval=10)
plt.show()

