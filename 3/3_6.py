def pluss(st):
    for i in range(1,len(st)-1):
        if st[i] != '+' and st[i+1] == '+' and st[i+1] == '+':
            return True
        else:
            return False


print(pluss('+2+23+4+578+43+ 3+'))