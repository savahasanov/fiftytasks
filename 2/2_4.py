spaces = 'удаление    пробелов'

def spacer(s):
    res = ""
    extra = False
    for i in s:
        if i != ' ':
            res += i
            ettra = False
        else:
            if not extra:
                res += i
                extra = True
    return res.strip()

print(spacer(spaces))
