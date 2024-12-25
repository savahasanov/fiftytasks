a = [2, 4, 6, 1, 7, 34, 9]

def med (n):
    for i in range(0, len(n)):
        for k in range(0, len(n)-1):
            if n[k] > n[k+1]:
                n[k],n[k+1] = n[k+1],n[k]


    return n[len(n)//2]
print(med(a))
