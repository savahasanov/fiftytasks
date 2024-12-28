from collections import Counter

def top3(st):
    st = st.replace(" ", "")
    count = Counter(st)
    enc = count.most_common(3)

    result = ', '.join(f'{let} - {num}' for let, num in enc)

    return result


print(top3('abababbahfhfhf'))

