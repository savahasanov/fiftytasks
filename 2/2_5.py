import math

r = 13
h = 14

def mass(rad, hei):
    v = math.pi * r**2 * h
    p = 1000
    m = v * p
    return round(m, 2)

m = mass(r, h)
print(f"Масса воды: {m} кг")