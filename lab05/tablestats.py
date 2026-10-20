# -------------------START HELPER FUNCTIONS-------------------
'''
Принимает строку из CSV-файла.
Возвращает список полей данной строки или None, если строка некорректна.
Поля разделены запятыми. Если внутри значения есть запятая, то все поле
должно быть заключено в двойные кавычки. Лишние пробельные символы до/после
запятой отсекаются. Строка считается некорректной, если двойных кавычек
нечетное число, т.е. экранирование некоторого поля осталось незакрытым.
'''
def parse_line(line: str) -> list:
    fields, field = [], ''
    count_quotes = 0
    line = line + ','  # последнее поле добавится в список в цикле
    for symb in line:
        if symb == '"':
            count_quotes += 1
        elif symb == ',' and count_quotes % 2 == 0:
            fields.append(field.strip())
            field = ''
        else:
            field += symb
    if count_quotes % 2 != 0:  # некорректная строка (например, '12,"34')
        return  # возвращается None
    return fields


'''
Принимает число и количество цифр после запятой (по умолчанию 0).
Возвращает данное число, округленное до требуемого количества цифр
после запятой по математическим правилам.
'''
def math_round(number: float, ndigits: int = 0) -> int | float:
    if not ndigits:
        return int(number + 0.5)
    return int(number * 10**ndigits + 0.5) / 10**ndigits
# --------------------END HELPER FUNCTIONS--------------------


'''
Принимает список строк CSV, где первая непустая строка — заголовок.
Возвращает список словарей с элементами вида {колонка: значение}.
Пустые и короткие строки пропускаются, пробелы вокруг значений отбрасываются.
'''
def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header, num_of_fields = None, 0
    for line in lines:
        record = parse_line(line)
        if record is None or not any(record):
            continue
        if header is None:
            header = record
            num_of_fields = len(header)
            continue
        if len(record) == num_of_fields:
            rows.append(dict(zip(header, record)))
    return rows


'''
Принимает список словарей с элементами вида {колонка: значение}.
Возвращает словарь, где ключ - тип записи, значение - число записей с данным типом.
'''
def count_types(rows: list[dict]) -> dict:
    counts = dict()
    for row in rows:
        curr_key = row['тип']
        if counts.get(curr_key) is None:
            counts[curr_key] = 0
        counts[curr_key] += 1
    return counts


'''
Принимает список словарей с элементами вида {колонка: значение} и тип записи.
Возвращает суммарную длительность (в минутах) записей одного типа,
округленную до десятых.
Нечисловое значение пропускается, а запятая считается десятичной точкой.
Если записей данного типа нет, функция возвращает 0.0.
'''
def total_minutes(rows: list[dict], kind: str) -> float:
    total_mins = 0.0
    for row in rows:
        if row['тип'] == kind:
            curr_mins = row['минуты'].replace(',', '.', 1)
            try:
                total_mins += float(curr_mins)
            except ValueError:
                pass
    return math_round(total_mins, 1)


'''
Принимает словарь с элементами вида {тип: количество}.
Возвращает сводку с заголовком "тип,количество" и записями (по алфавиту типа).
Строки разделяются символом переноса строки.
'''
def to_csv(counts: dict) -> str:
    result = ['тип,количество']
    counts = dict(sorted(counts.items()))
    for type, count in counts.items():
        result.append(f'{type},{count}')
    return '\n'.join(result)


if __name__ == '__main__':
    lines = [
        '\n',
        '          \n',
        'дата,тип,минуты\n',
        '2026-03-01,запуск,1.5\n',
        '2026-03-01,проверка,3,4\n',
        '2026-03-01,запуск,abc\n',
        '2026-03-01,ошибка,"0.4\n',
        '2026-03-02,проверка,"2,5"\n',
        '2026-03-02,ошибка,0.4\n',
        '2026-03-02,запуск,"1,2"\n',
        '  2026-03-03, проверка ,  2.5 \n',
        '2026-03-03,запуск,1.2\n'
        ]
    rows = read_rows(lines)
    print('-> Считанные строки:')
    for row in rows:
        print(row)
    counts = count_types(rows)
    print('-> Количество записей каждого типа:')
    print(counts)
    print('-> Суммарная длительность записей одного типа:')
    print('запуск:', total_minutes(rows, 'запуск'))
    print('выгрузка:', total_minutes(rows, 'выгрузка'))
    print('-> Итоговая сводка:')
    print(to_csv(counts))