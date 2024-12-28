def help_bool(a):
    rude = {
        'к': 'Коммутативность',
        'а': 'Ассоциативность',
        'д': 'Дистрибутивность',
        'м': 'Законы де Мо́ргана'
    }
    rudefind = rude[a]
    if rudefind:
        return rudefind
    else:
        return 'Выберите букву к, а, д или м'

print(help_bool('к'))