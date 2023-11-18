import sys
import configparser as cfg
from conway import board, plotting

input_file = sys.argv[1]

config = cfg.ConfigParser()
config.read(input_file)

nrows = config.getint("board_dimensions", "nrows")
ncols = config.getint("board_dimensions", "ncols")
random_seed = config.getint("board_dimensions", "random_seed")

nsteps = config.getint("output", "nsteps")
fps = config.getint("output", "fps")

output_filename = (
    config.get("output", "output_path")
    + "/"
    + config.get("output", "filename")
    + "_"
    + str(nrows)
    + "_"
    + str(ncols)
    + "_"
    + str(random_seed)
    + "_"
    + str(nsteps)
)

myBoard = board.Board((nrows, ncols), random_seed)
plotting.generate_gif_episode(myBoard, nsteps, fps, output_filename)
