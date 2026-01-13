

# N-Body Simulation -- Project

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
![](https://github.com/AndersenFred/Datenverarbeitung/nbody.gif)