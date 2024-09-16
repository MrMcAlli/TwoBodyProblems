import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D


#Two Body problem example using the Earth and a satalite as example bodies
ert_rad = 6378.0 #km
ert_mu = 398600.0 # km^3 / s^2


# t - Time ; y - State ; mu - extra
def diff_eq(t,y,mu):
    #unpack state
    rx,ry,rz,vx,vy,vz=y
    r = np.array([rx,ry,rz])

    #radius vector norm
    norm_r = np.linalg.norm(r)

    #two body acceleration
    ax,ay,az = -r*mu/norm_r**3

    return [vx,vy,vz,ax,ay,az]

if __name__ == "__main__":
    # initial orbit parameters
    r_mag = ert_rad+500.0 #km
    v_mag = np.sqrt(ert_mu/r_mag) #in km/s

    #initial position and velocity vectors
    r0 = [r_mag,0,0]
    v0 = [0,v_mag,0]

    #timespan 
    tspan = 100*60.0
    dt = 100.0

    n_steps = int(np.ceil(tspan/dt))

    #initialize arrays
    ys = np.zeros((n_steps, 6))
    ts = np.zeros((n_steps, 1))

    #initial conditions
    y0 = r0+v0
    ys[0] = np.array(y0)
    step = 1

    #initialize solver
    solver = ode(diff_eq)
    solver.set_integrator('lsoda')
    solver.set_initial_value(y0,0)
    solver.set_f_params(ert_mu)

    #propagate orbit

    while solver.successful() and step < n_steps:
        solver.integrate(solver.t+dt)
        ts[step]=solver.t
        ys[step]=solver.y
        step+=1
        print(step)

rs = ys[:,:3]

fig = plt.figure

plt.plot(rs)
plt.show()