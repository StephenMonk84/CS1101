def print_strings():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        if letter == 'O' or letter =='Q':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)

print_strings()