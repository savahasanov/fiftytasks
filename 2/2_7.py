def all (box):
    all = 0
    for i in box:
        a, b, h = i
        volume = a * b * h
        all += volume
    return all

sizes = [(33, 3, 12), (3, 56, 1), (2, 5, 5)]

sum = all(sizes)
print(sum)