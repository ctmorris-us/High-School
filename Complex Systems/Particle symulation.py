import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n_particles = 1000

sd = .1


fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(-10, 10), ax.set_xticks([])
ax.set_ylim(-10, 10), ax.set_yticks([])


particles = np.zeros(n_particles, dtype=[('position', float, 2)])
particles['position'] = np.random.randn(n_particles,2)

scat = ax.scatter(particles['position'][:,0], particles['position'][:,1],s=10,lw=.5,edgecolors=[0,0,0,1],
                  facecolors='purple')

def update(data):
    t = data
    particles['position'] += np.random.normal(0,.2,(n_particles,2))
    scat.set_offsets(particles['position'])

animation = FuncAnimation(fig, update,interval = 50)
plt.show()








#####
Gravity Simulation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


n_parts = 50
size = 10
G = 105
Dt = .05
n_particles = 1000
sd = .1


particles = np.zeros(n_particles, dtype=[('position', float, 2)])
particles['position'] = np.random.randn(n_particles,2)


def init_particles():
    global particles, ones


    particles = np.zeros((n_parts, 1), dtype=[('x_position', float, 1), ('y_position', float, 1), ('mass', float, 1),
                                         ('acceleration', float, 2), ('velocity', float, 2) ])
    ones = np.diag([1] * n_parts)

    particles['mass'] = np.random.randint(1,10)

    particles['x_position'] = np.random.randn(n_parts,1) * size
    particles['y_position'] = np.random.randn(n_parts,1) * size

    particles['velocity'][:,:,0] = np.zeros((n_parts,1))
    particles['velocity'][:,:,1] = np.zeros((n_parts,1))

    particles['acceleration'][:, :, 0] = np.zeros((n_parts, 1))
    particles['acceleration'][:, :, 1] = np.zeros((n_parts, 1))


def update_particles(t):
    global particles, ones

    foo = t

    particles_temp = np.zeros((n_parts, n_parts), dtype = [('d_v', float, 2), ('distance', float, 2),
            ('force_vectors', float, 2), ('sign', int, 2), ('mass_product', float, 1)])

    particles_temp['d_v'][:,:,0] = np.add(-1 * particles['x_position'], particles['x_position'].T)
    particles_temp['d_v'][:,:,1] = np.add(-1 * particles['y_position'], particles['y_position'].T)

    particles_temp['mass_product'] = np.dot(particles['mass'], particles['mass'].T)

    particles_temp['sign'][:,:,0] = np.sign(particles_temp['d_v'][:,:,0])
    particles_temp['sign'][:,:,1] = np.sign(particles_temp['d_v'][:,:,1])

    particles_temp['distance'][:,:,0] = ((1 / (particles_temp['d_v'][:,:,0] + ones) **2 ) - ones) \
                                               * particles_temp['sign'][:,:,0]
    particles_temp['distance'][:,:,1] = ((1 / (particles_temp['d_v'][:,:,1] + ones) **2 ) - ones) \
                                               * particles_temp['sign'][:,:,1]

    particles_temp['force_vectors'][:,:,0] = (G * particles_temp['mass_product'][:,0] *
                                                    particles_temp['distance'][:,:,0])
    particles_temp['force_vectors'][:,:,1] = (G * particles_temp['mass_product'][:,0] *
                                                    particles_temp['distance'][:,:,1])

    particles['acceleration'][:,:,0] = np.sum(particles_temp['force_vectors'][:,:,0], axis=1).reshape(n_parts,1) / particles['mass']
    particles['acceleration'][:,:,1] = np.sum(particles_temp['force_vectors'][:,:,1], axis=1).reshape(n_parts,1) / particles['mass']

    particles['velocity'][:,:,0] = particles['acceleration'][:,:,0] * Dt + particles['velocity'][:,:,0]
    particles['velocity'][:,:,1] = particles['acceleration'][:,:,1] * Dt + particles['velocity'][:,:,1]

    particles['x_position'] = particles['velocity'][:,:,0] * Dt + particles['x_position']
    particles['y_position'] = particles['velocity'][:,:,1] * Dt + particles['y_position']

    scat.set_offsets(np.concatenate((particles['x_position'], particles['y_position']), axis = 1))



fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(-1000, 1000), ax.set_xticks([])
ax.set_ylim(-1000, 1000), ax.set_yticks([])

scat = ax.scatter(particles['x_position'][:,0], particles['y_position'][:,0],s=particles['mass']*50,lw=.5,edgecolors=[0,0,0,1],
                  facecolors='purple')

animation = FuncAnimation(fig, update_particles, init_func=init_particles,interval = 100)
plt.show()


def test():
    init_particles()
    print(particles['x_position'])
    print(particles['y_position'])
    x = 1
# Control C intrupts while loop
    while x != 0:
        x = input('bwah:' )

        update_particles(1)
        print(particles['x_position'])
        print(particles['y_position'])
