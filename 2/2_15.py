friends = ['Sasha', 'Masha', 'Natasha', 'Pasha']
enemies = ['Pasha', 'Masha']

def truefriends (friends, enemies):
    return [friend for friend in friends if friend not in enemies]

print(truefriends(friends, enemies))
