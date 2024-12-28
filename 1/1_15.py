from audioop import reverse

def list_sort(lst):
    lst.sort(reverse = True)
    return lst

lst = [3, 5, 6, 1, 2]

print(list_sort(lst))