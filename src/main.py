import numpy as np
from conway import board
from conway import plotting

myBoard1 = board.Board(
    np.array(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
myBoard2 = board.Board((30, 50))
plotting.plot_episode(myBoard2, 200, 10, "gol_anim.gif")
