import numpy as np

myCheckBoard = np.zeros((8, 8), dtype=int)
myCheckBoard[::2, 1::2] = 1
myCheckBoard[1::2, ::2] = 1

print(myCheckBoard)
