def lucker(n):
    n = n/2
    n = int(n)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range (0,10**n):
        for k in range (0,10**n):
            i = str (i)
            k = str (k)
            for num in i:
                sum2 += int(num)
            for num in k:
                sum3 += int(num)
            if sum3 == sum3:
                sum1 += 1
            sum2 = 0
            sum3 = 0

    return sum1

print(lucker(1))