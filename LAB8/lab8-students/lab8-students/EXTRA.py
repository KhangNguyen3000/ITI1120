def move_zeros_v1(x):
    tmp = []
    c = 0
    for i in (x):
        if (i != 0):
            tmp.append(i)
        else:
            c = c + 1
    for x in range (c):
        tmp.append(0)
    return tmp

def move_zeros_v2(x):
    tmp = []
    c = 0
    for i in (x):
        if (i != 0):
            tmp.append(i)
        else:
            c = c + 1
    for k in range (c):
        tmp.append(0)
    for i in range(len(x)):
        x[i] = tmp[i]

def moves_zeros_v3(x):
    c = x.count(0)
    for i in range (c):
        x.remove(0)
        x.append(0)
