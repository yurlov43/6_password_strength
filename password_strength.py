import sys
import re
import getpass
from string import punctuation


def open_black_list(filepath="pass.txt"):
    with open(filepath, "r", encoding="utf-8-sig") as black_list:
        return black_list.read()


def estimate_password_length(
        user_password,
        rating,
        short_length=5,
        average_length=10):
    if short_length < len(user_password) <= average_length:
        rating += 1
    if average_length < len(user_password):
        rating += 2
    return rating


def symbol_groups_serch(user_password, rating):
    if re.search(r"[a-z]+", user_password):
        rating += 1
    if re.search(r"[A-Z]+", user_password):
        rating += 2
    if re.search(r"[0-9]+", user_password):
        rating += 2
    if re.search(r"[{}]+".format(punctuation), user_password):
        rating += 2
    return rating

if __name__ == '__main__':
    user_password = getpass.getpass("Введите пароль: ")
    if user_password:
        black_list = open_black_list()
        if user_password not in black_list.split():
            rating = 1
            rating = estimate_password_length(user_password, rating)
            rating = symbol_groups_serch(user_password, rating)
        else:
            sys.exit("Ошибка: введённый пароль не допустим.")
    else:
        sys.exit("Ошибка: пароль не введён.")
    print(
        "Сложность пароля оценивается на {} балла(ов) из 10".format(rating))
