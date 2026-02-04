
## Before you start (Git & SSH)

If you have never used Git with SSH before, follow these guides **once**:

* Generate and register an SSH key:
  [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

* First-time Git setup:
  [https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

---

## Project structure

```
.
├── environment.yml     # Conda environment (name: DV)
├── demo.py             # Example N-body simulation
├── Visualizer.py       # Visualization class (creates GIF animations)
└── README.md
```

---

## Installation (Conda environment)

 **Only run this on your personal computer (not on CIP).**

1. Open a terminal in the project directory.

2. Create the environment:

   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:

   ```bash
   conda activate DV
   ```

All required packages (NumPy, Matplotlib, Pillow) are now installed.

---

## Using Git

Clone the repository to your local machine:

```bash
git clone git@github.com:AndersenFred/Datenverarbeitung.git
cd Datenverarbeitung
```

Create your own working branch:

```bash
git checkout -b <your-branch-name>
```

Work **only on your own branch**.
Once you have implemented new features:

```bash
git checkout main
git merge <your-branch-name>
```

## Running the demo

After activating the environment:

```bash
python demo.py
```

When the script finishes, a file called

```
nbody.gif
```

will appear in the project directory.

Example output:

![](https://github.com/AndersenFred/Datenverarbeitung/blob/main/nbody.gif)

---

## VS Code (CIP)

On CIP systems, load and start VS Code using:

```bash
module load vscode
code
```

---

# Collision formular
```latex
p_i+p_j&\to p_i'+p_j'\\
n_{ij}&=\frac{x_i-x_j}{||x_i-x_j||}\\
v_i'&=v_i-\frac{2m_j}{m_i+m_j}[(v_i-v_j)\cdot n_{ij}]n_{ij}\\
v_j'&=v_j-\frac{2m_i}{m_i+m_j}[(v_j-v_i)\cdot n_{ji}]n_{ji}
```

## Extension ideas
(Coding a Physics Engine from scratch!)[https://www.youtube.com/watch?v=nXrEX6j-Mws]

```text
- [ ] Reflecting walls → clamp positions at box edges, flip velocity component
- [ ] Periodic boundaries → modulo position by box size
- [ ] Central force (harmonic trap) → add F = -k r to acceleration
- [ ] Lennard–Jones–type force → pairwise force with cutoff radius
- [ ] Velocity-dependent drag → add F = -γ v
- [ ] External constant field → add uniform acceleration (e.g. gravity)
- [ ] Two-species particles → store type array, condition forces on type
- [ ] Soft collisions → short-range repulsive force instead of hard contact
- [ ] Hard-sphere collisions → detect overlap, swap normal velocity components
- [ ] Random kicks (noise) → add small Gaussian velocity increments
- [ ] Initial condition presets → lattice, ring, or disk setups
```

## Analysis ideas


```text
- [ ] Total energy vs time → compute kinetic + potential energy
- [ ] Momentum conservation → sum m·v and check constancy
- [ ] Center-of-mass motion → track COM position and velocity
- [ ] Speed distribution → histogram of |v|
- [ ] Pair distance distribution → histogram of |r_i − r_j|
- [ ] Radial density profile → bin particles by distance from origin
- [ ] Timestep dependence → compare results for different dt
- [ ] Collision rate → count collision events per unit time
- [ ] Energy exchange → track kinetic energy per particle
- [ ] Equilibration time → detect when observables stabilize
- [ ] Chaos indicator (qualitative) → compare nearby initial conditions
```


