import numpy as np


class Board:
    def __init__(self, initialisation):
        if isinstance(initialisation, np.ndarray):
            self.data = initialisation
        elif type(initialisation) is tuple:
            self.data = 1 * (np.random.rand(*initialisation) > 0.5)
        else:
            self.data = 1 * (np.random.rand(*6, 6) > 0.5)
