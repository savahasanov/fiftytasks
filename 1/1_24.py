def camel(st):
    number = 0
    word = ''
    for let in st:
        if  let.isalpha():
            if number == 0:
                let = let.upper()
                word += let
                number = 1
            elif number == 1:
                letter = let.lower()
                word += let
                number = 0
        else:
            word += let

    return word

print(camel("jjjj djjfdjldj djjfd"))