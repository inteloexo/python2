#Apskaiciuoti nurodytoje direktorijoje esanciu failu statistika ir ja isvesti i faila.
#Statistika: pirmiausia isvesti bendrai visuose failuose kokie ir kiek kartu
#pasikartoja a) zodziai b) simboliai. Antra, i ta pati faila isvesti ta pacia
#statistika apskaiciuota kiekvienam failui atskirai.
#Author - Mantas Gedrimas


import os
import sys


def get_dir_file_paths(path):
    file_paths = os.listdir(path)

    for item in file_paths:
        if not(os.path.isfile(item)):
            file_paths.remove(item)

    return file_paths

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
                    if symbol in symbols_dict:
                        symbols_dict[symbol] = symbols_dict[symbol] + 1
                    else:
                        symbols_dict[symbol] = 1

        opened_file.close()
    return symbols_dict


def write_to_file(output, **kwargs):
    for key in kwargs:
       output.write("'%s' - %s\n" % (key, kwargs[key]))

def main():
    if len(sys.argv) == 3:
        if os.path.isdir(sys.argv[1]):
            file_paths = get_dir_file_paths(sys.argv[1])
            results_file = open(sys.argv[2], 'w')

            for file in file_paths:
                words_count = get_words_count(file)
                symbols_count = get_symbols_count(file)

                results_file.write("Statistics of file '%s':"
                               "\nWords:\n" % (file))
                write_to_file(results_file, **words_count)
                results_file.write("Symbols:\n")
                write_to_file(results_file, **symbols_count)

            words_count = get_words_count(*file_paths)
            symbols_count = get_symbols_count(*file_paths)

            results_file.write("Statistics of all files from directory '%s':"
                                "\nWords:\n" % sys.argv[2])
            write_to_file(results_file, **words_count)
            results_file.write("Symbols:\n")
            write_to_file(results_file, **symbols_count)

            results_file.close()
        else:
            print("Directory does not exist!")
    else:
        print("Error! Incorrect number of given parameters.")


if __name__ == "__main__":
    main()