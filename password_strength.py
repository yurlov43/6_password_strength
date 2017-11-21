import sys
import re
import getpass


def search_in_black_sheet(user_password):
    with open("pass.txt", "r", encoding="utf-8-sig") as passwords:
        if user_password in passwords.read().split():
            return False
    return True


def estimate_password_length(user_password, rating=1):
    if 5 < len(user_password) <= 10:
        rating = 2
    if 10 < len(user_password):
        rating = 3
    return rating


def symbol_groups_serch(user_password, rating=0):
    if re.search(r"[a-z]+", user_password):
        rating += 1
    if re.search(r"[A-Z]+", user_password):
        rating += 1
    if re.search(r"[0-9]+", user_password):
        rating += 1
    if re.search(r"[!@#$%^&*-]+", user_password):
        rating += 1
    return rating


def estimate_grouping(user_password, rating=1):
    groups_in_password = re.finditer(
        r"(?P<lower_case>[a-z]+)"
        "|(?P<uppercase>[A-Z]+)"
        "|(?P<digits>[0-9]+)"
        "|(?P<special_symbols>[!@#$%^&*-]+)",
        user_password)
    groups_number = len(list(groups_in_password))
    if 2 < groups_number <= 4:
        rating = 2
    if 4 < groups_number:
        rating = 3
    return rating

if __name__ == '__main__':
    user_password = getpass.getpass("Введите пароль: ")
    print(user_password)
    if user_password:
        if search_in_black_sheet(user_password):
            rating = estimate_password_length(user_password)
            rating += symbol_groups_serch(user_password)
            rating += estimate_grouping(user_password)
        else:
            sys.exit("Ошибка: введённый пароль не допустим.")
    else:
        sys.exit("Ошибка: пароль не введён.")
    print(
        "Сложность пароля оценивается на {} балла(ов) из 10".format(rating))
