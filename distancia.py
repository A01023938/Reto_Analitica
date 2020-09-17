import numpy as np

# 1

list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]

def distance(list1, list2):
    if len(list1) != len(list2):
        return -1
    d_squared = 0
    for v1, v2 in zip(list1, list2):
        d_squared += (v2 - v1)**2

    return d_squared**(1/2)

# 2

puntos = [[2,2], [4,4], [5,5], [14,14], [16,16]]
centros = [[3,3], [15,15]]

def cercanos(puntos, centros):
    clusters = [[] for _ in range(0, len(centros))]
    for i, punto in enumerate(puntos):
        p_vs_c = []
        for i, centro in enumerate(centros):
            d = distance(centro, punto)
            p_vs_c.append(d)
        pos = p_vs_c.index(min(p_vs_c))
        clusters[pos].append(punto)

    return clusters
   
        
# 3

def centers(clusters):
    new_centers = []
    for cluster in clusters:
        c = [sum(x) for x in zip(*cluster)]
        for i, _ in enumerate(c):
            c[i] /= len(cluster)
        new_centers.append(c)
    return new_centers

print(centers(cercanos(puntos, centros)))