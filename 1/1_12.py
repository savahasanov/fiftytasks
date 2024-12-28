def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)

change([3, 45, 6, 7])