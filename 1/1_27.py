def cleaned_str (st):
    a = ''
    for i in st:
        if i =='@':
            a = a[:-1]
        else:
            a += i

    return a


print(cleaned_str('гр@оо@лк@оц@ва'))