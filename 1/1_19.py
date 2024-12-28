def count_it(sequence):
    counter = {}

    for num in sequence:
        if num.isdigit():
            number = int(num)
            if number in counter:
                counter[number] += 1
            else:
                counter[number] = 1

    sort = sorted(counter.items(), key = lambda item: item[1], reverse = True)
    three = dict(sort[:3])

    return three

print(count_it('8746328746832785472984574679278468392746382576987345'))


