def letter(n):
    a = 'abcdefghiklmnopqrstuvwxyz'
    cou = 0
    for let in n:
        for i in range (len(a)):
            if let == a[i]:
                cou += i+1
    return cou


print(letter('dfhhs'))