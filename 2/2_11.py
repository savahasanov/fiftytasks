num1 = [1,3,4,23,56]
num2 = [1,4,3,2]

def up(n):
    for i in range(1, len(n)):
        if n[i] <= n[i-1]:
            return 'Не возрастает'
    return 'Возрастает'

print(up(num1))
print(up(num2))