a = 'ababaababa'
b = 'ababa'
def two (n):
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            return True
    return False

print(two(a))
print(two(b))