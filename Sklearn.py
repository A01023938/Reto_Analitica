from sklearn.cluster import KMeans
from LoadData import load_data
import matplotlib.pyplot as plt
import numpy as np 



if __name__ == "__main__":


    filepath = './data/iris.data'

    data = load_data(filepath)

    X = np.array([f[:-1] for f in data])
    Y = np.array([f[-1] for f in data]) # Target

    kmeans = KMeans(n_clusters=3).fit(X)

    print('Label')
    print(kmeans.labels_)
    print('')
    print(kmeans.cluster_centers_)

    plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')
    plt.show()