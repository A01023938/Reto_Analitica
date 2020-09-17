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

def distance(list_x, list_y):
    if len(list_x) != len(list_y):
        return -1

    d_squared = 0
    for v1, v2 in zip(list_x, list_y):
        d_squared = (v1 - v2)**2
        d_squared += (v2 - v1)**2

    return d_squared**(1/2)



distance(list_x,list_y)





