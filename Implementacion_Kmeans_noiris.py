import numpy as np
import random

# 1

def distance(a, b):
    return np.sqrt(np.sum((np.array(b)-np.array(a))**2))
    

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
    

def k_means(puntos, times):
    cx = int(input("How many centers would you like to generate?:"))
    centros = []
    for i in range(cx+1):
        n = ((random.randint(1,15),(random.randint(1,50))))
        centros.append(n)
    #centros = [[2,3],[32,29]]
    clusters = get_clusters(puntos,centros)

    for i in range(times):
        clusters = get_clusters(puntos,centros)
        centros = center(clusters)
    print("Clusters: ", clusters)
    print("Centros: ", centros)
    print("Puntos: ", puntos)



if __name__ == "__main__":
    
    
    cx = int(input("How many coordinates would you like to generate?:"))
    puntos = []
    ci = int(input("How many times would you like the centers to be readjusted?: "))
    for i in range(cx+1):
        n = ((random.randint(1,15),(random.randint(1,50))))
        puntos.append(n)
    print(k_means(puntos,ci))

    
