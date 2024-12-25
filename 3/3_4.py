cards = [3, 5, 10, 2, 6]

def carder(cards):
    summ = sum(cards)
    return summ > 21

print(carder(cards))