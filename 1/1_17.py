def to_dict(lst):
    dict = {}
    for name in lst:
        dict[name] = name
    return dict

print(to_dict(['name']))