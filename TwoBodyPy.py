import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# initial positions and velocities of the two bodies
x1, y1, z1 = 0.00, 0.00, 0.00
vx1, vy1, vz1 = 0.001, -0.001, 0.001

x2, y2, z2 = -0.005, -0.005, 0.005
vx2, vy2, vz2 = -0.01, 0.01, -0.0001

# masses of the two bodies
m1 = 0.5 
m2 = 0.7 


# Set up the constants for the simulation
G = 6.67430e-11  # Gravity
dt = 0.01  # Time step

# Set up the arrays to store the positions of the two bodies over time
X1, Y1, Z1 = [x1], [y1], [z1]
X2, Y2, Z2 = [x2], [y2], [z2]

# simulation loop
for _ in range(100*60):
    # r = the distance between the two bodies
    r = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    
    if r == 0:
        break

    # Calculate the gravitational force between the two bodies
    fx = G * m1 * m2 * (x2 - x1) / r**3
    fy = G * m1 * m2 * (y2 - y1) / r**3
    fz = G * m1 * m2 * (z2 - z1) / r**3

    # Update the velocities 
    vx1 += fx / m1 * dt
    vy1 += fy / m1 * dt
    vz1 += fz / m1 * dt

    vx2 -= fx / m2 * dt
    vy2 -= fy / m2 * dt
    vz2 -= fz / m2 * dt

    # Update the positions 
    x1 += vx1 * dt
    y1 += vy1 * dt
    z1 += vz1 * dt

    x2 += vx2 * dt
    y2 += vy2 * dt
    z2 += vz2 * dt

    # Add the new positions to the arrays
    X1.append(x1)
    Y1.append(y1)
    Z1.append(z1)

    X2.append(x2)
    Y2.append(y2)
    Z2.append(z2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the positions of the two bodies over time
ax.plot(X1, Y1, Z1, 'r-', label='Body 1')
ax.plot(X2, Y2, Z2, 'b-', label='Body 2')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
