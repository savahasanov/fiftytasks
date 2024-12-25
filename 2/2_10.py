
def sum(number):
    summ = []
    res = 0

    for i in numbers:
        res += i
        summ.append(res)
    return summ

numbers = [1, 2, 3]
result = sum(numbers)

print(result)
