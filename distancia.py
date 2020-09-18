import numpy as np

# 1

def distance(list1, list2):
    if len(list1) != len(list2):
        return -1
    d_squared = 0
    for v1, v2 in zip(list1, list2):
        d_squared += (v2 - v1)**2

    return d_squared**(1/2)

# 2


def get_clusters(puntos, centros):
    # Puntos es un lista de puntos (x,y)
    # Centro es una lista de k listas (x,y)

    clusters = [[] for _ in range(0, len(centros))]

    for punto in puntos:
        # Tengo un punto que lo quiero comparar contra todos los centros
        # Aqui se van a guardar todas las distancias entre mi punto y todos los centros
        p_vs_c = []
        for centro in centros:
            d = distance(centro, punto)
            p_vs_c.append(d)
        # la minima distancia entre mi punto y todos los centros es el la key del centro correcto
        pos = p_vs_c.index(min(p_vs_c)) # La posicion del centro en clusters
        clusters[pos].append(punto)

    return clusters

# 3

def center(cluster):
    for i in cluster:
        cluster_f = []
        for i in range(len(cluster)):
            avg = np.mean(cluster[i], axis=0)
            #avgr = avg.astype(int) Turns list to ints
            cluster_f.append(avg.tolist())
    return cluster_f
    

puntos = [(32,34),(2,1),(9,7)]
centros = [[3,3], [15,15]]

values = get_clusters(puntos, centros)
print("Clusters: ", values)

average = center(values)
print("Average of cluster values for new centers: ", average)