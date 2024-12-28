def first_last(letter,st):
    first = None
    last = None
    let = []
    st = st.lower()

    for i in range (len(st)):
        if st[i] == letter:
            let.append(i)

    if let != []:
        first = let[0]
        last = let[-1]
    return first,last
print(first_last('m','mygygitytytyutytyfmj'))