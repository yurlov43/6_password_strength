import sys
import re


def search_password_list(user_password):
    with open("pass.txt", "r", encoding="utf-8-sig") as passwords:
        if user_password in passwords.read().split():
            return False
    return True


def get_password_strength(password):
    rating = 0
    if 1 <= len(password) <= 5:
        rating += 1
    if 5 < len(password) <= 10:
        rating += 3
    if 10 < len(password):
        rating += 5
    if re.search(r"[a-z]", user_password):
        rating += 1
    if re.search(r"[A-Z]", user_password):
        rating += 1
    if re.search(r"[0-9]", user_password):
        rating += 1
    if re.search(r"[!@#$%^&*-]", user_password):
        rating += 1
    return rating


if __name__ == '__main__':
    user_password = input("Введите пароль: ")
    if user_password:
        rating = get_password_strength(user_password)
    else:
        sys.exit("Ошибка: пароль не введён.")
    if search_password_list(user_password):
        rating = get_password_strength(user_password) + 1
    else:
        sys.exit("Ошибка: введённый пароль не допустим.")
    print(
        "Сложность пароля оценивается на \
        {} балла(ов) из 10".format(rating))
