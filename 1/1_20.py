dictionary = {
    'key1': 'a',
    'key2': 'b',
    'key3': 'c',
    'key4': 'd',
    'key5': 'e'
}

print(dictionary)

lst = list(dictionary.items())
lst[0], lst[-1] = lst[-1], lst[0]

dictionary = dict(lst)

del dictionary[list(dictionary.keys())[1]]

dictionary['new_key'] = 'new_value'

print(dictionary)

