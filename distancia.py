list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]

def distance(list1, list2):
    if len(list1) != len(list2):
        return -1
    d_squared = 0
    for v1, v2 in zip(list1, list2):
        d_squared += (v2 - v1)**2

    return d_squared**(1/2)

print(distance(list1, list2))