"""
    ---Task 3---
    Добавьте в пакет, созданный на семинаре шахматный модуль.
  Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих
друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""


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


def main():
    arrangement = []
    for _ in range(8):
        x, y = map(int, input().split())
        arrangement.append((x, y))

    if is_valid_queens(arrangement):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()
