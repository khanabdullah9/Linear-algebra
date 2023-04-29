import numpy as np
from diagonalization import diagonanlize



if __name__ == "__main__":
    T = np.array([[1, 2], [3, 4]])
    print(diagonanlize(T,2))