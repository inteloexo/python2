#Apskaičiuoti nurodytoje direktorijoje esančių failų statistiką ir ją išvesti į failą.
#Statistika: pirmiausia išvesti bendrai visuose failuose kokie ir kiek kartų
#pasikartoja a) žodžiai b) simboliai. Antra, į tą patį failą išvesti tą pąčią
#statistiką apskaičiuotą kiekvienam failui atskirai.
#Author - Mantas Gedrimas


import os
import sys
import string

def get_dir_filepaths(path):
    return os.listdir(path)