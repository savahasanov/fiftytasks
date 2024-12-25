def correct(s):
    word = ''
    pun = ''
    punfind = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '!' and not punfind:
            pun = '!'
            punfind = True

        elif s[i] == '?' and not punfind:
            pun = '?'
            punfind = True

        elif s[i] != '!' and s[i] != '?':
            word += s[i]

    word = word[::-1] + pun
    return word

print(correct("Не ори!!!!!"))
