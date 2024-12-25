str = 'jdhj4jkk123hjkh34jhk2kjhkjh43'

def summa(s):
    tot = 0
    num = ''

    for i in s:
        if i.isdigit():
            num += i
        else:
            if num:
                tot += int(num)
                num = ''

    if num:
        tot += int(num)
    return tot

print(summa(str))
