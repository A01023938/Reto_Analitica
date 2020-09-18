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


def centre(puntos, centros):
    # Puntos es un lista de puntos (x,y)
    # Centro es una lista de k listas (x,y)

    clusters = [[] for _ in range(0, len(centros))]

    for i, punto in enumerate(puntos):
        # Tengo un punto que lo quiero comparar contra todos los centros
        # Aqui se van a guardar todas las distancias entre mi punto y todos los centros
        p_vs_c = []
        for i, centro in enumerate(centros):
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
            avgr = avg.astype(int)
            cluster_f.append(avgr.tolist())
    print(cluster_f)
    

list_x = []
list_y = []
num = int(input("Please input the size of the lists: "))
c1 = 0

while c1 < num:
    x = int(input(f"Input x {c1} value: "))
    y = int(input(f"Input y {c1} value: "))
    list_x.append(x)
    list_y.append(y)
    c1 = c1+1

puntos = zip(list_x,list_y)
#print(tuple(puntos))
centros = [[3,3], [15,15]]

values = centre(tuple(puntos), centros)
print(values)

center(values)












