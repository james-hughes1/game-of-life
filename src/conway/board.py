"""!@file board.py
@brief Module containing tools for handling the board

@details Contains a class Board with a constructor and step method.
@author Created by J. Hughes on 17/11/2023.
"""

# Import modules
from typing import Union
import numpy as np
from scipy.signal import convolve2d


class Board:
    """!@brief Object instantiating the current state of a game of life
    episode.

    @details Constructor method is passed initialisation parameter to set up
    the initial board state. Contains a step method which evolves the episode
    by a single step.
    """

    def __init__(self, start: Union[np.ndarray, tuple], random_seed: int = 42):
        """!@brief Constructor to instantiate board with initial state.

        @param start If a numpy array is given, this is used for the
        board data. If a tuple is given, a numpy array of this shape is
        generated for the board data.
        @param random_seed Provides random seed for board generation
        reproducibility.
        """
        random_gen = np.random.default_rng(seed=random_seed)
        if isinstance(start, np.ndarray):
            if len(start.shape) != 2:
                raise ValueError("Invalid start, must be 2d array.")
            elif (start * (1 - start) != 0).any():
                raise ValueError("Invalid start, entries must be 0 or 1.")
            self.data = start
        elif type(start) is tuple:
            if len(start) != 2:
                raise ValueError("Invalid start, must be 2-tuple.")
            elif not (isinstance(start[0], int) and isinstance(start[1], int)):
                raise ValueError("Invalid start, must be tuple of ints.")
            self.data = random_gen.integers(low=0, high=2, size=start)
        else:
            raise TypeError("Invalid start, must be 2d np.array or tuple.")
        self.nrows, self.ncols = self.data.shape

    def __str__(self):
        """!@brief String method for Board object.

        @details Enables board data to be printed to stdout in a somewhat
        user-friendly grid.

        @return display_str The full board grid output as a string.
        """
        display_list = []
        for row in self.data:
            row_list = []
            # Each row is converted into a str like "X|X|_" for 1, 1, 0.
            for entry in row:
                if entry == 1:
                    row_list.append("X")
                else:
                    row_list.append("_")
            display_list.append("|".join(row_list))
        display_str = "\n".join(display_list)
        return display_str

    def step(self):
        """!@brief Evolves the board by one time-step.

        @details The board is evolved according to Conway's original Game of
        Life rules:
        - Live cells with more than 3 neighbours die (overpopulation);
        - Live cells with fewer than 2 neighbours die (underpopulation);
        - Dead cells with exactly 3 neighbours become alive (reproduction).
        Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        """
        # Compute the matrix where each entry is the number of neighbours.
        neighbour_filter = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbours = convolve2d(
            self.data, neighbour_filter, mode="same", boundary="wrap"
        )
        # Compute the matrix of cells which are live in the next step.
        living_old = ((neighbours == 2) | (neighbours == 3)) & (self.data == 1)
        living_new = (neighbours == 3) & (self.data == 0)
        self.data = 1 * (living_old + living_new)
