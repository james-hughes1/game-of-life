import numpy as np
from scipy.signal import convolve2d


class Board:
    def __init__(self, initialisation):
        if isinstance(initialisation, np.ndarray):
            self.data = initialisation
        elif type(initialisation) is tuple:
            self.data = 1 * (np.random.rand(*initialisation) > 0.5)
        else:
            self.data = 1 * (np.random.rand(*6, 6) > 0.5)

    def step(self):
        neighbour_filter = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbours = convolve2d(
            self.data, neighbour_filter, mode="same", boundary="wrap"
        )
        living_old = ((neighbours == 2) | (neighbours == 3)) & (self.data == 1)
        living_new = (neighbours == 3) & (self.data == 0)
        self.data = 1 * (living_old + living_new)
