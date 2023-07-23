"""
    ---Task 1_1---
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""


def _is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(date_string):
    try:
        day, month, year = map(int, date_string.split('.'))
        if 1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
            if month == 2 and day == 29:
                return _is_leap_year(year)

            if month in [4, 6, 9, 11] and day == 31:
                return False

            if month == 2 and day > 29:
                return False

            return True
        else:
            return False
    except ValueError:
        return False