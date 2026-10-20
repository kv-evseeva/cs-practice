from tablestats import *

table_path = input('Введите путь к таблице: ')

try:
    with open(table_path, 'r', encoding='utf-8') as table:
        rows = read_rows(table)
except FileNotFoundError:
    print("Данной таблицы не существует")
else:
    print('Число прочитанных записей:', len(rows))
    counts = count_types(rows)
    print('Число различных типов:', len(counts))
    print('Суммарные минуты записей типа "ошибка":', total_minutes(rows, 'ошибка'))

    with open('summary.csv', 'w', encoding='utf-8') as out:
        out.write(to_csv(counts))
