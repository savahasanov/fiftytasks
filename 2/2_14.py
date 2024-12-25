a = 'Первернул он ее перевернул'

def swapper(st):
    swapped = st[::-1]
    res = swapped.swapcase()
    return res

print(swapper(a))
