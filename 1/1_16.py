def all_eq(lst):
    maxx = max(len(s) for s in lst)
    res = [s.ljust(maxx, '_') for s in lst]
    return res

lst = ['okokokokok' , 'okok', 'ok' ]
print(all_eq(lst))