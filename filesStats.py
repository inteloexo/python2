#Apskaičiuoti nurodytoje direktorijoje esančių failų statistiką ir ją išvesti į failą.
#Statistika: pirmiausia išvesti bendrai visuose failuose kokie ir kiek kartų
#pasikartoja a) žodžiai b) simboliai. Antra, į tą patį failą išvesti tą pąčią
#statistiką apskaičiuotą kiekvienam failui atskirai.
#Author - Mantas Gedrimas


import os


def get_dir_filepaths(path):
    return os.listdir(path)

def get_words_count(*args):
    words_dict = {}

    for file in args:
        opened_file = open(file, 'r')

        for line in opened_file:
            words = line.split()

            for word in words:
                if word in words_dict:
                    words_dict[word] = words_dict[word] + 1
                else:
                    words_dict[word] = 1

    opened_file.close()
    return words_dict


def get_symbols_count(*args):
    symbols_dict = {}

    for file in args:
        opened_file = open(file, 'r')

        for line in opened_file:
            for symbol in line:
                if symbol != ' ':
                    if symbol in dict:
                        symbols_dict[symbol] = symbols_dict[symbol] + 1
                    else:
                        symbols_dict[symbol] = 1

    opened_file.close()
    return symbols_dict