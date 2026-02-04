import numpy as np
from tqdm import tqdm
from Visualizer import Visualizer
import utils

def collision(v: np.array, x: np.array, m: np.array, r: np.array, stability: float=1e-12) -> np.array:
    '''
    input
        v: np.array (N,2)
        m: np.array (N,2)
        r: np.array (N,2)
    '''
    v_new = np.copy(v)
    for i in range(0, len(r)):
        for j in range(i + 1, len(r)):
            if np.sum((x[i] - x[j])**2) < (r[i]**2 + r[j]**2):
                n_ij = (x[i] - x[j]) / np.sqrt(np.sum((x[i] - x[j])**2))
                v_new[i] = v[i] - ((2 * m[j]) / (m[i] + m[j] + stability)) * np.dot(v[i] - v[j], n_ij) * n_ij
                v_new[j] = v[j] - ((2 * m[i]) / (m[i] + m[j] + stability)) * np.dot(v[j] - v[i], -n_ij) * (-n_ij)
    return v_new


def acceleration(pos, velocity, masses):
    '''May the force be with you'''
    return np.random.normal(0, 10, size=np.shape(pos))

def box_edge(pos, velecoty):
    '''Flip velecoty when at edges'''
    return pos, velecoty 



def main():
    utils.set_latex_style(False)
    mass = 1
    N = 300
    masses = np.ones(N)
    steps = 4000
    dt = 2e-3
    m = 10
    box_size = 500
    eps = 2e-2
    pos = np.random.normal(0, 100, size=(N,2))# positions
    vel = np.random.normal(0, 100, size=(N,2))# velocity
    viz = Visualizer(N, trail=0, interval_ms=30, marker_size=18, xlim=(-box_size, box_size), ylim=(-box_size, box_size))
    for step in tqdm(range(steps)):
        # kick
        a = acceleration(pos, vel, mass)
        vel = vel + 0.5 * a * dt
        #vel = collision(v, pos, masses, )
        pos = pos + vel * dt
        pos, vel = box_edge(pos, vel)
        if step % m == 0:
            viz.capture(pos, t=step * dt)
        # update positions and velocitys
    viz.show()
if __name__ == "__main__":
    main()
