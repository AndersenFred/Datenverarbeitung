import numpy as np
import matplotlib.pyplot as plt
import utils
from matplotlib.animation import FuncAnimation, PillowWriter

class Visualizer:
    """
    2D visualization utility for N-body simulations.

    This class collects phase-space snapshots (particle positions in 2D)
    during a numerical integration and post-processes them into an animated
    GIF. It is designed for workflows where visualization is triggered
    sparsely (e.g., every m timesteps) to avoid unnecessary overhead during
    time integration.

    Notes
    -----
    - The class stores only the frames explicitly captured via ``capture``.
    - Rendering is deferred until ``make_animation`` or ``save_gif`` is called.
    - Animation is based on ``matplotlib.animation.FuncAnimation`` with a
      ``PillowWriter`` backend for GIF output.
    """

    def __init__(
        self,
        N,
        xlim=None,
        ylim=None,
        dpi=120,
        marker_size=12,
        trail=0,               # number of previous captured frames to show as faint trail
        interval_ms=30,        # playback interval between frames
        equal_aspect=True,
    ):
        """
        Initialize the visualizer.

        Parameters
        ----------
        N : int
            Number of bodies to visualize.
        xlim : tuple(float, float), optional
            Fixed x-axis limits. If ``None``, limits are inferred from data.
        ylim : tuple(float, float), optional
            Fixed y-axis limits. If ``None``, limits are inferred from data.
        dpi : int, optional
            Resolution of the figure in dots per inch.
        marker_size : float, optional
            Marker area (in points^2) for each body in the scatter plot.
        trail : int, optional
            Number of previously captured frames to display as faint trails.
            A value of 0 disables trails.
        interval_ms : int, optional
            Delay between animation frames in milliseconds.
        equal_aspect : bool, optional
            If True, enforce equal scaling on both axes.
        """
        self.N = int(N)
        self.frames = []       # list of (N,2) arrays
        self.times = []        # optional
        self.trail = int(trail)
        self.interval_ms = int(interval_ms)

        self.fig, self.ax = plt.subplots(dpi=dpi, figsize=(6.4, 6.4))
        if equal_aspect:
            self.ax.set_aspect("equal", adjustable="box")
        utils.prettify_axes(self.ax)
        self._xlim = xlim
        self._ylim = ylim

        self.scat = self.ax.scatter([], [], s=marker_size)
        self.time_text = self.ax.text(
            0.02, 0.98, "", transform=self.ax.transAxes, va="top"
        )

        self._trail_lines = []
        if self.trail > 0:
            for _ in range(self.trail):
                (ln,) = self.ax.plot([], [], lw=1, alpha=0.25)
                self._trail_lines.append(ln)

        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")

    def capture(self, positions, t=None):
        """
        Store a snapshot of particle positions.

        This method is intended to be called intermittently during the
        integration loop (e.g., every m timesteps).

        Parameters
        ----------
        positions : array_like, shape (N, 2)
            Cartesian coordinates of all bodies at the current timestep.
        t : float, optional
            Physical time associated with this snapshot. If ``None``,
            the frame index is displayed instead.
        """
        p = np.asarray(positions, dtype=float)
        if p.shape != (self.N, 2):
            raise ValueError(f"positions must have shape ({self.N}, 2); got {p.shape}")
        self.frames.append(p.copy())
        self.times.append(None if t is None else float(t))

    def _infer_limits_if_needed(self):
        """
        Infer axis limits from stored frames if no fixed limits were supplied.

        The limits are chosen to enclose all captured positions with a small
        padding to avoid clipping at the edges.
        """
        if (self._xlim is not None) and (self._ylim is not None):
            self.ax.set_xlim(*self._xlim)
            self.ax.set_ylim(*self._ylim)
            return

        allp = np.concatenate(self.frames, axis=0)  # (len(frames)*N, 2)
        xmin, ymin = np.min(allp, axis=0)
        xmax, ymax = np.max(allp, axis=0)

        dx = xmax - xmin
        dy = ymax - ymin
        pad_x = 0.05 * (dx if dx > 0 else 1.0)
        pad_y = 0.05 * (dy if dy > 0 else 1.0)

        if self._xlim is None:
            self.ax.set_xlim(xmin - pad_x, xmax + pad_x)
        else:
            self.ax.set_xlim(*self._xlim)

        if self._ylim is None:
            self.ax.set_ylim(ymin - pad_y, ymax + pad_y)
        else:
            self.ax.set_ylim(*self._ylim)

    def _init_anim(self):
        """
        Initialize the animation artists.

        Returns
        -------
        tuple
            Artists that are re-drawn for blitting.
        """
        self.scat.set_offsets(np.empty((0, 2)))
        self.time_text.set_text("")
        for ln in self._trail_lines:
            ln.set_data([], [])
        return (self.scat, self.time_text, *self._trail_lines)

    def _update(self, i):
        """
        Update all artists for frame ``i``.

        Parameters
        ----------
        i : int
            Frame index.

        Returns
        -------
        tuple
            Updated artists for blitting.
        """
        p = self.frames[i]
        self.scat.set_offsets(p)

        if self.times[i] is None:
            self.time_text.set_text(f"frame {i+1}/{len(self.frames)}")
        else:
            self.time_text.set_text(f"t = {self.times[i]:.6g}")

        if self.trail > 0:
            for k, ln in enumerate(self._trail_lines, start=1):
                j = i - k
                if j >= 0:
                    pj = self.frames[j]
                    ln.set_data(pj[:, 0], pj[:, 1])
                else:
                    ln.set_data([], [])
        return (self.scat, self.time_text, *self._trail_lines)

    def make_animation(self):
        """
        Construct a Matplotlib animation object from captured frames.

        Returns
        -------
        matplotlib.animation.FuncAnimation
            Animation object suitable for display or saving.

        Raises
        ------
        RuntimeError
            If no frames have been captured.
        """
        if len(self.frames) == 0:
            raise RuntimeError("No frames captured. Call capture(...) during the simulation.")
        self._infer_limits_if_needed()
        return FuncAnimation(
            self.fig,
            self._update,
            frames=len(self.frames),
            init_func=self._init_anim,
            interval=self.interval_ms,
            blit=True,
        )

    def save_gif(self, path="nbody.gif", fps=30):
        """
        Save the captured animation to a GIF file.

        Parameters
        ----------
        path : str, optional
            Output filename for the GIF.
        fps : int, optional
            Frames per second in the resulting animation.

        Returns
        -------
        str
            Path to the written GIF file.
        """
        anim = self.make_animation()
        writer = PillowWriter(fps=fps)
        anim.save(str(path), writer=writer)
        return str(path)

    def show(self):
        """
        Display the animation in an interactive window.

        This method is primarily intended for exploratory use in scripts
        or interactive sessions. For reproducible output, prefer
        ``save_gif``.
        """
        _ = self.make_animation()
        plt.show()
