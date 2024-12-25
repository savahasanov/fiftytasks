money = [3, 4, 3, 5, 1]

def cou(money):
    summa = sum(money)
    return summa % 3 == 0
res = cou(money)

if res:
    print('Можно')
else:
    print('Нельзя')




