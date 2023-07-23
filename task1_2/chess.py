"""
    ---Task 3---
    Добавьте в пакет, созданный на семинаре шахматный модуль.
  Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих
друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""

import random

MAX_ATTEPMTS = 1_000_000
def is_valid_queens(arrangement):
    def is_diagonal(x1, y1, x2, y2):
        return abs(x1 - x2) == abs(y1 - y2)

    for i in range(8):
        for j in range(i + 1, 8):
            x1, y1 = arrangement[i]
            x2, y2 = arrangement[j]
            if x1 == x2 or y1 == y2 or is_diagonal(x1, y1, x2, y2):
                return False
    return True


def random_queens_arrangement():
    queens = [(x, y) for x in range(1, 9) for y in range(1, 9)]
    random.shuffle(queens)
    return queens[:8]


def main():
    successful_arrangements = 0
    attempts = 0

    while successful_arrangements < 1 and attempts < MAX_ATTEPMTS:
        arrangement = random_queens_arrangement()
        if is_valid_queens(arrangement):
            successful_arrangements += 1
            print(f"Успешная расстановка {successful_arrangements}: {arrangement}")
        attempts += 1
        if attempts == MAX_ATTEPMTS - 1:
            print('Комбинация не найдена.')


if __name__ == "__main__":
    main()
