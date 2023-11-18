"""!@file plotting.py

@brief Contains tools for plotting conway's game of life.

@author Created by J. Hughes on 17/11/2023.
"""

# Import plotting modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MultipleLocator
from board import Board


def generate_gif_episode(
    board: Board, nsteps: int, fps: int, filename: str, gridlines: bool = False
):
    """!@brief Generate a gif for an episode of Game of Life.

    @param board An object of class Board, storing the current state of the
    board.
    @param nsteps Number of steps to be generated in the episode.
    @param fps Number of frames per second for the .gif file.
    @param filename Filename for the .gif file.
    @param gridlines Boolean controlling whether to add lines around the border
    of each cell.
    """
    fig = plt.figure()
    ax = plt.axes()
    fig.set_tight_layout(True)

    # Plot gridlines if specified
    if gridlines:
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.grid(which="major", color="blue")
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
    else:
        ax.axis("off")
    extent_zeroed_cells = (0, board.ncols, 0, board.nrows)
    im = plt.imshow(board.data, cmap="gnuplot", extent=extent_zeroed_cells)

    # Controls update of frames
    def animate_func(i):
        board.step()
        im.set_array(board.data)
        return [im]

    # Generate animation
    anim = animation.FuncAnimation(
        fig,
        animate_func,
        frames=nsteps,
        interval=1000 / fps,
    )

    anim.save("plots/" + filename, fps=fps)
