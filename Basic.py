from LoadData import load_data
from distancia import distance, get_clusters, center
import matplotlib.pyplot as plt
import numpy as np

COLORS = [
    'tab:blue',
    'tab:orange',
    'tab:green',
    'tab:red',
    'tab:purple',
    'tab:brown',
    'tab:pink',
    'tab:gray',
    'tab:olive',
    'tab:cyan',
]

def k_means(points, k, iterations=10):
    """
    K Means Unsupervised ML Algorithm Implementation with Forgy Initialization
    Input:
        points (numpy array): a 2D Array with the data to cluster.
        k (int): The number of clusters to find
    """
    
    idx = np.random.randint(len(points),size=k)
    
    centroids = points[idx,:]
    
    clusters = get_clusters(points,centroids)

    for i in range(iterations):

        clusters = get_clusters(points,centroids)
        centroids = center(clusters)

    return clusters,centroids

if __name__ == "__main__":

    filepath = './data/iris.data'

    data = load_data(filepath)

    X = np.array([f[:-1] for f in data])
    Y = np.array([f[-1] for f in data]) # Target

    clusters,centroids = k_means(X,3)
    print(centroids)

    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(
            cluster[:,0],
            cluster[:,1],
            c = COLORS[i],
            label="Cluster {}".format(i)
        )

    for i, centroid in enumerate(centroids):
        plt.scatter(
            centroid[0],
            centroid[1],
            c = COLORS[i],
            marker='x',
            s=100
        )

    plt.show()

    

