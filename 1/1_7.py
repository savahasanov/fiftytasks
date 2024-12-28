def mul_to_int(a,b):
    s = a * b
    if float(s).is_integer():
        return int(s)
    return s

print(mul_to_int(4,7.5))