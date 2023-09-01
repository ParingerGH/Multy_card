from typing import DefaultDict
import argparse
from colorama import Fore
from datetime import datetime
import os

# Задаем аргумент пути к файлу
parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True, type=str, help="Путь до файла")
args = vars(parser.parse_args())
file_path = os.path.abspath(args['file'])

# ВЫход если путь не корректный
if not os.path.exists(file_path):
    print(f"{Fore.RED}[ERROR]{Fore.RESET} File {file_path} doesn't exist")
    exit(1)

# Задаем промежутки допустимых кодов знаков
ranges = [
    (65,91), # Заглавная латиница A-Z
    (97,123) # Строчная латиница z-a
]

# Заполняем список допустимых кодов знаков
accepted_chars = set()
for char_range in ranges:
    accepted_chars.update([x for x in range(*char_range)])

def main() -> dict[str,int]:

    # Заполняем словарь читая файл по 1 символу
    letters = DefaultDict(lambda : 0)

    with open(file_path, 'r') as f:

        while True:
            char = f.read(1)
            if not char:
                break

            # проверяя что знак валидный с помощью accepted_chars
            if ord(char) in accepted_chars:
                letters[char.lower()] += 1

    return dict(letters)

if __name__ == "__main__":
    start = datetime.now()
    print(f"Letters in file {file_path}\n")
    for letter, count in main().items():
        print(f"{letter} : {count}")
    print(f"\nExecution time: {(datetime.now()-start).total_seconds()} sec.")
