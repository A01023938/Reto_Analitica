
import numpy as np


if __name__ == "__main__":
    
    filepath = './data/iris.data'

    with open(filepath, 'r') as fp:
        data = fp.read()

    X = np.array(f[:-1] for f in data)
    Y = np.array(f[-1] for f in data)

    
    
    