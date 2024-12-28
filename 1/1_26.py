def shortener(st):
    brackets = False
    word = ''
    for i in st:
        if i == '(':
            brackets = True
        elif i == ')':
            brackets = False
        elif not brackets:
            word += i

    return word.strip()


print(shortener('aaa (,e,e,e) nnn'))