import sys
import re
import getpass
from string import punctuation


def open_black_list(filepatch="pass.txt"):
    with open(filepatch, "r", encoding="utf-8-sig") as black_list:
        return black_list.read()


def estimate_password_length(
        user_password,
        rating,
        small_length=5,
        average_length=10):
    if small_length < len(user_password) <= average_length:
        rating += 1
    if average_length < len(user_password):
        rating += 2
    return rating


def symbol_groups_serch(user_password, rating):
    """Поиск в пароле символов различных групп"""
    # поиск строчных букв
    if re.search(r"[a-z]+", user_password):
        rating += 1
    # поиск заглавных букв
    if re.search(r"[A-Z]+", user_password):
        rating += 1
    # поиск цифр
    if re.search(r"[0-9]+", user_password):
        rating += 1
    # поиск спец символов, например, !@#$%^&*()-
    if re.search(r"[{}]+".format(punctuation), user_password):
        rating += 1
    return rating


def estimate_grouping(
        user_password,
        rating,
        no_division_into_groups=0,
        small_number_of_groups=2,
        large_number_of_groups=4):
    """Поиск в пароле групп различных символов. Например,
    DSFdfdDSFsd - 4 группы чередующихся строчных и заглавных букв"""
    password_pattern = re.compile(r"""
        ([a-z]+)  #поиск группы строчных букв
        |([A-Z]+) #поиск группы заглавных букв
        |([0-9]+) #поиск группы цифр
        |([{}]+)  #поиск группы спец. символов, например, !@#$%^&*()-
        """.format(punctuation), re.X)
    groups_in_password = password_pattern.finditer(user_password)
    groups_number = len(list(groups_in_password))
    if no_division_into_groups < groups_number <= small_number_of_groups:
        rating += 1
    if small_number_of_groups < groups_number <= large_number_of_groups:
        rating += 2
    if large_number_of_groups < groups_number:
        rating += 3
    return rating

if __name__ == '__main__':
    user_password = getpass.getpass("Введите пароль: ")
    if user_password:
        black_list = open_black_list()
        if user_password not in black_list.split():
            rating = 1
            rating = estimate_password_length(user_password, rating)
            rating = symbol_groups_serch(user_password, rating)
            rating = estimate_grouping(user_password, rating)
        else:
            sys.exit("Ошибка: введённый пароль не допустим.")
    else:
        sys.exit("Ошибка: пароль не введён.")
    print(
        "Сложность пароля оценивается на {} балла(ов) из 10".format(rating))
