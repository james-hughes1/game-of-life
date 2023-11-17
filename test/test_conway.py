import numpy as np
from src.conway import board


# The following three tests are patterns taken from
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns


def test_loaf():
    initial_state = np.array(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
    loaf = board.Board(initial_state)
    for _ in range(10):
        loaf.step()
    assert (loaf.data == initial_state).all()


def test_beacon():
    initial_state = np.array(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
    beacon = board.Board(initial_state)
    beacon.step()
    assert (beacon.data != initial_state).any()
    beacon.step()
    assert (beacon.data == initial_state).all()


def test_glider():
    initial_state = np.array(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
    glider = board.Board(initial_state)
    for _ in range(24):
        glider.step()
    assert (glider.data == initial_state).all()


def test_random():
    rand_board = board.Board((4, 7))
    rand_board.step()
    assert rand_board.data.shape == (4, 7)
