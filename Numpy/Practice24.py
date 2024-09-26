# Using Numpy, create an 8x8 array with a checkerboard pattern of 0s and 1s, like a chessboard.

import numpy as np

checkboard_tile=np.array([[0,1],[1,0]])

checkboard=np.tile(checkboard_tile,(4,4))

print(checkboard)