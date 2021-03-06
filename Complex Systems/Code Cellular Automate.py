
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



n, m = 100, 100
cell = np.random.randint(0,2,(n,m))

import matplotlib
from matplotlib import *

fig = plt.figure(figsize=(7, 7))
# ax = fig.add_axes([0, 0, 1, 1], frameon=False)
#
# locations = np.argwhere(cell)
# scat = ax.scatter(locations[:,0], locations[:,1], s = 10, lw= 3,facecolor = 'black')
im = imshow(cell, vmin=0,vmax=1,cmap=cm.binary)

def update_cell(data):
    global cell
    q = data
    x, y = cell.shape
    temp_cell = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            neighborhood = cell[max(i-1,0):i+2,max(j-1,0):j+2]
            ##^^ System for strict boundary (I don't even think that the Max is necessary)
            #neighborhood = cell[(i-1) % x: (i+2) % x, (j-1) % y: (j+2) % y]
            ## ^ system for periodic (torodial boundary)
            if neighborhood.sum() > 4:
            #if neighborhood.sum() >= int(np.size(neighborhood) / 2):
                temp_cell[i,j] = 1
            else:
                #temp_cell[i,j] = cell[i,j]
                temp_cell[i,j] = 0
    cell = temp_cell.astype(int)
    #temp_locations = np.argwhere(cell)
    # scat.set_offsets(temp_locations)
    im.set_array(cell)

animation = FuncAnimation(fig, update_cell,interval=10)
plt.show()


# e = d.reshape(np.size(d)) for Neumann neighborhoods and significantly more complicated


#Waves is excitable media problem

#Assume a two-dimensional space made of cells where each cell takes either a normal (0; quiescent), excited (1),
# or refractory (2, 3, . . . k) state. A normal cell becomes excited stochastically with a probability determined
# by a function of the number of excited cells in its neighbor- hood. An excited cell becomes refractory (2) immediately,
# while a refractory cell remains refractory for a while (but its state keeps counting up) and then it comes back
# to normal after it reaches k

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

n, m = 100, 100
k = 7
R_excited = 1
R_refactory = 3
W_excited = .2
W_refactory= .5
media = np.zeros((n, m), dtype = [('value', int, 2), ('color', float, 4)])
media_copy = np.zeros((n,m))



def init_function():
    global media, media_copy, im, fig
    media = np.zeros((n, m), dtype = [('value', int, 2), ('color', float, 4)])
    #media['value'][:,:,0] = np.random.randint(0, 2, (n, m,))
    media['value'][25:30,25:30,0] = 1
    media['value'][75:80,75:80,0] = 1

    media['value'][:,:,1] = 1
    media['color'][:,:,3] = (1/media['value'][:,:,1])*media['value'][:,:,0]
    media_copy = np.zeros((n,m))

fig = plt.figure(figsize=(7, 7))
im = plt.imshow(media['color'])


def update_function(frames):
    global media
    q = frames
    # dummy variable with no purpose but to fit into animation function semantics
    for x in range(n):
        for y in range(m):
            if media['value'][x,y,1] == k:
                media_copy[x,y] = 0
            elif media['value'][x,y,0] == 0:

                value_excited = np.sum(media['value'][(x - R_excited) % n : (x+R_excited+1) % n , (y-R_excited) % m : (y+1+R_excited) % m, 0])
                ###value_refactory = np.sum(media['value'][(x - R_refactory) % n : (x+R_refactory+1) % n , (y-R_refactory) % m : (y+1+R_refactory) % m, 0]) - value_excited
                # ^^ Periodic Boundary

                #value_excited = np.sum(media['value'][(x - R_excited): (x + R_excited + 1), (y - R_excited): (y + 1 + R_excited), 0])
                #value_refactory = np.sum(media['value'][(x - R_refactory): (x + R_refactory + 1), (y - R_refactory): (y + 1 + R_refactory), 0]) - value_excited

                ## ^^ Stationary Boundary

                ###value_excited, value_refactory = equalize(value_excited, value_refactory)
                ###value_total = 1 if ((value_excited*W_excited - value_refactory*W_refactory) > random.random()) else 0
                value_total = 1 if ((value_excited * W_excited)  > random.random())*9 else 0
                media_copy[x,y] = value_total
            else:
                media_copy[x,y] = 1
    media['value'][:,:,0] = media_copy
    media['color'][:,:,3] = (1/media['value'][:,:,1])*media['value'][:,:,0]
    media['value'][:, :, 1] = (media['value'][:, :, 0] * media['value'][:, :, 1]) + 1
    #1*0+1
    im.set_array(media['color'])



animation = FuncAnimation(fig, update_function, frames=None, init_func=init_function, interval=500)
plt.show()


### For analyzing the function
def plot_media():
    plt.figure(figsize=(7, 7))
    plt.imshow(media['color'])
    plt.show()

def analyze_media():
    update_function(1)
    plot_media()



def equalize(value_e, value_r):
    value_e = value_e/(value_e + value_r + 1)
    value_r = value_r/(value_e + value_r + 1)
    return value_e, value_r




# ##
# ####
# #
# say
