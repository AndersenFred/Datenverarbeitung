
from matplotlib.ticker import LogLocator, NullFormatter, AutoMinorLocator
import matplotlib as mpl


def prettify_axes(ax, xlog=False, ylog=False, grid=False):
    """Consistent axis formatting (minor ticks, log locators, optional light grid)."""
    if xlog:
        ax.set_xscale("log")
        ax.xaxis.set_major_locator(LogLocator(base=10.0))
        ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs=(0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9)))
        ax.xaxis.set_minor_formatter(NullFormatter())
    else:
        ax.xaxis.set_minor_locator(AutoMinorLocator())

    if ylog:
        ax.set_yscale("log")
        ax.yaxis.set_major_locator(LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=(0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9)))
        ax.yaxis.set_minor_formatter(NullFormatter())
    else:
        ax.yaxis.set_minor_locator(AutoMinorLocator())

    if grid:
        ax.grid(True, which="major", linewidth=0.5, alpha=0.25)
        ax.grid(True, which="minor", linewidth=0.4, alpha=0.15)

    ax.tick_params(which="both")
def set_latex_style(use_tex: bool = True, base_fontsize: float = 11.0):
    """
    LaTeX-like Matplotlib styling:
      - 10pt fonts (LaTeX article default)
      - Computer Modern via usetex (if available) or CM mathtext fallback
      - consistent ticks, lines, legend, savefig defaults
    """
    mpl.rcParams.update({
        # Text / fonts
        "text.usetex": bool(use_tex),
        "font.family": "serif",
        "font.size": base_fontsize,
        "axes.labelsize": base_fontsize,
        "axes.titlesize": base_fontsize,
        "legend.fontsize": base_fontsize * 0.90,
        "xtick.labelsize": base_fontsize * 0.90,
        "ytick.labelsize": base_fontsize * 0.90,
        "text.latex.preamble": r'\usepackage[dvips]{graphicx}\usepackage{xfrac}\usepackage{ amssymb }',
        "mathtext.fontset": "cm",
        "font.serif": ["Computer Modern Roman", "CMU Serif", "DejaVu Serif"],

        # Lines
        "lines.linewidth": 1.6,
        "lines.markersize": 4.0,

        # Axes / ticks
        "axes.linewidth": 0.8,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.size": 4.0,
        "ytick.major.size": 4.0,
        "xtick.minor.size": 2.0,
        "ytick.minor.size": 2.0,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
        "xtick.minor.width": 0.6,
        "ytick.minor.width": 0.6,
        "xtick.top": True,
        "ytick.right": True,

        # Legend
        "legend.frameon": False,
        "legend.handlelength": 2.2,
        "legend.handletextpad": 0.6,
        "legend.labelspacing": 0.4,

        # Figure / export
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.08,
    })
