import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MultipleLocator


def plot_episode(board, n, fps, filename, gridlines=False):
    fig = plt.figure()
    ax = plt.axes()

    fig.set_tight_layout(True)

    nrows, ncols = board.data.shape

    if gridlines:
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.grid(which="major", color="blue")
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
    else:
        ax.axis("off")

    im = plt.imshow(board.data, cmap="gnuplot", extent=(0, ncols, 0, nrows))

    def animate_func(i):
        if i % fps == 0:
            print(".", end="")

        board.step()

        im.set_array(board.data)
        return [im]

    anim = animation.FuncAnimation(
        fig,
        animate_func,
        frames=n,
        interval=1000 / fps,
    )

    anim.save("plots/" + filename, fps=fps)
