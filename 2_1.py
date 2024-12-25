x = [8, 99, 45]
y = [2, 5, 76]
def pointer(x, y):
    coord = []
    for i in range(len(x)):
        coord.append((x[i], y[i]))
    return coord
print(pointer(x, y))