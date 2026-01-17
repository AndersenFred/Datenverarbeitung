

# N-Body Simulation -- Project
[https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
[https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

## Project structure

```
.
├── environment.yml     # Conda environment (name: DV)
├── demo.py             # Example N-body simulation
├── Visualizer.py        # Visualizer class (creates GIF animations)
└── README.md
```

---


## Installation (Conda environment)
Only at home, not in Cip
1. Open a terminal in the project directory.

2. Create the environment:

   ```bash
   conda env create -f environment.yml
   ```

3. Activate it:

   ```bash
   conda activate DV
   ```

That’s it. All required packages (NumPy, Matplotlib, Pillow) are now available.

---
## using git
```bash
git clone git@github.com:AndersenFred/Datenverarbeitung.git # this copies the procject to you local computer
git checkout -b <your branch>
```

Once you have included some features
```bash
git checkout main
git merge
```

## Running the demo

After activating the environment:

```bash
python demo.py
```

When the script finishes, you will find:

```
nbody.gif
```

in the project directory.
![](https://github.com/AndersenFred/Datenverarbeitung/blob/main/nbody.gif)

# VS Code
For loading
```bash
module load vscode
```
and then for launching it
```bash 
code
```

# Ideas
- [ ] Reflecting walls $\to$ clamp positions at box edges, flip velocity component
- [ ] Periodic boundaries $\to$ modulo position by box size
- [ ] Central force (harmonic trap) $\to$ add F = -k r to acceleration
- [ ] Lennard–Jones–type force $\to$ pairwise force with cutoff radius
- [ ] Velocity-dependent drag $\to$ add F = -$\gamma$ v
- [ ] External constant field $\to$ add uniform acceleration (e.g. gravity)
- [ ] Two-species particles $\to$ store type array, condition forces on type
- [ ] Soft collisions $\to$ short-range repulsive force instead of hard contact
- [ ] Hard-sphere collisions $\to$ detect overlap, swap normal velocity components
- [ ] Random kicks (noise) $\to$ add small Gaussian velocity increments
- [ ] Initial condition presets $\to$ functions for lattice, ring, or disk setups


# Analysis ideas
- [ ] Total energy vs time $\to$ compute kinetic + potential each step, plot drift
- [ ] Momentum conservation $\to$ sum $m\cdot v$ and check constancy
- [ ] Center-of-mass motion $\to$ track COM position and velocity
- [ ] Speed distribution $\to$ histogram of |v| at fixed times
- [ ] Pair distance distribution $\to$ histogram of |r_i − r_j|
- [ ] Radial density profile $\to$ bin particles by distance from origin
- [ ] Timestep dependence $\to$ repeat run with different dt and compare outcomes
- [ ] Collision rate $\to$ count overlaps or collision events per unit time
- [ ] Energy exchange $\to$ track kinetic energy per particle over time
- [ ] Equilibration time $\to$ monitor when macroscopic quantities stabilize
- [ ] Chaos indicator (qualitative) $\to$ compare two nearby initial conditions
