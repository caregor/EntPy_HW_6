from task1_2 import task1_1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    date = '29.02.2001'
    if task1_1.is_valid_date(date):
        print(f"{date} - Дата существует.")
    else:
        print(f"{date} - Некорректная дата.")