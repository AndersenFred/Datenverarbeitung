import numpy as np
from tqdm import tqdm
from Visualizer import Visualizer
import utils

def accel_gravity(pos, mass, G=1.0, eps=1e-2):
    """
    Naive O(N^2) gravitational acceleration with Plummer softening.
    pos: (N,2), mass: (N,)
    returns a: (N,2)
    """
    N = pos.shape[0]
    a = np.zeros_like(pos)
    for i in range(N):
        r = pos - pos[i]                         # (N,2)
        dist2 = np.sum(r*r, axis=1) + eps*eps    # (N,)
        inv_dist3 = dist2**(-1.5)
        inv_dist3[i] = 0.0
        # a_i = G * sum_j m_j * (r_ij) / |r_ij|^3
        a[i] = G * np.sum((mass[:, None] * r) * inv_dist3[:, None], axis=0)
    return a

def main():
    utils.set_latex_style(False)
    # --- simulation parameters
    N = 300
    steps = 4000
    dt = 2e-3
    m = 10               # capture every m timesteps
    G = 1.0
    eps = 2e-2

    rng = np.random.default_rng(0)

    # --- initial conditions (roughly bound "cloud")
    mass = rng.uniform(0.5, 2.0, size=N)
    pos = rng.normal(scale=5, size=(N, 2))
    vel = rng.normal(scale=3, size=(N, 2))

    # remove net momentum
    vel -= np.average(vel, axis=0, weights=mass)

    # --- visualizer
    viz = Visualizer(N, trail=0, interval_ms=30, marker_size=18)

    # --- velocity Verlet integration
    a = accel_gravity(pos, mass, G=G, eps=eps)

    for step in tqdm(range(steps)):
        # drift
        pos = pos + vel * dt + 0.5 * a * dt * dt
        # kick
        a_new = accel_gravity(pos, mass, G=G, eps=eps)
        vel = vel + 0.5 * (a + a_new) * dt
        a = a_new

        if step % m == 0:
            viz.capture(pos, t=step * dt)
    viz.show()
    #out = viz.save_gif("nbody.gif", fps=30)
    #print(f"Wrote {out}")

if __name__ == "__main__":
    main()
