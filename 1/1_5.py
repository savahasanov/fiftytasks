def to_float(n):
    if type(n) == int:
        n = float(n)
    else:
        print('Невозмоно преобразовать')
    return n

print ((to_float(34)))