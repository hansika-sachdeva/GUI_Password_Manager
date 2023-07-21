from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['#', '@', '$', '%', '&', '*', '!', '-']


def generate_password():
    nr_letters = randint(6, 8)
    nr_symbols = randint(1, 3)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    return password
