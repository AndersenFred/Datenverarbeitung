import numpy as np
from tqdm import tqdm
from Visualizer import Visualizer
import utils


def acceleration(pos, velocity, masses):
    '''May the force be with you'''
    return np.random.normal(0, 1, size=np.shape(pos))

def box_edge(pos, velecoty, box_size):
    '''Flip velecoty when at edges'''
    if_edge = (pos[:,0]<box_size[0][0]) | (pos[:,0]>box_size[0][1])
    velecoty[if_edge, 0] *= -1
    pos[if_edge, 0] *= 0.99
    if_edge = (pos[:,1]<box_size[1][0]) | (pos[:,1]>box_size[1][1])
    velecoty[if_edge, 1] *= -1
    pos[if_edge, 1] *= 0.99
    return pos, velecoty 


def collision(m: np.array, x: np.array, v: np.array, r: np.array, stability: float=1e-12) -> np.array:
    '''
    input:
        v: np.array (N,2)
        x: np.array (N,2)
        m: np.array (N,)
        r: np.array (N,)
        stability float: numerical factor for stability default 1e-12
    '''
    
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            if np.sum((x[i]-x[j])**2<(r[i]**2+r[j]**2)):
                n = (x[i]-x[j])/(np.linalg.norm(x[i]-x[j])+stability)
                v[i] = v[i] - (2*m[j])/((m[i]+m[j])+stability)*np.dot((v[i]-v[j]),n)*n
                v[j] = v[j] - (2*m[i])/((m[i]+m[j])+stability)*np.dot((v[j]-v[i]),-n)*(-n)
            
    return v
def main():
    utils.set_latex_style(False)
    mass = 1
    N = 30
    steps = 4000
    dt = 2e-3
    m = 1
    radius = np.ones(N) * 0.1
    masses = np.random.random(N)
    box_size = ((-100,100),(-100,100))
    eps = 2e-2
    pos = np.random.normal(0, 100, size=(N,2))# positions
    vel = np.random.normal(0, 100, size=(N,2))# velocity
    viz = Visualizer(N, trail=0, interval_ms=30, marker_size=18, xlim=(box_size[0][0], box_size[0][1]), ylim=(box_size[1][0], box_size[1][1]))
    for step in tqdm(range(steps)):
        # kick
        a = acceleration(pos, vel, mass)
        vel = vel + 0.5 * a * dt
        pos = pos + vel * dt
        pos, vel = box_edge(pos, vel, box_size)
        vel = collision(masses, pos, vel,radius )
        if step % m == 0:
            viz.capture(pos, t=step * dt)
        # update positions and velocitys
    viz.show()
if __name__ == "__main__":
    main()
