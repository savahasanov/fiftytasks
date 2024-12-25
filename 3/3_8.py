def difficulter(password):
    res = 0
    leng = 0
    special = 0
    capital = 0
    dig = 0
    low = 0

    for i in password:
        if not i.isalpha() and not i.isdigit():
            special = 1
        if i.isupper():
            capital = 1
        if i.islower():
            low = 1
        if i.isdigit():
            dig = 1
    if len(password) >= 7:
        leng = 1
    summ = special + capital + dig + low + leng
    return summ
print(difficulter('1jdhfjkhkslk>kfj!@'))


