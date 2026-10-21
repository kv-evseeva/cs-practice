'''
Принимает список значений.
Возвращает словарь с элементами вида {значение: количество},
подсчитывая, сколько раз встречается каждое значение.
'''
def count_items(values: list) -> dict:
    counts = dict()
    for val in values:
        counts[val] = counts.get(val, 0) + 1
    return counts


'''
Принимает список значений.
Возвращает список уникальных значений в порядке возрастания.
'''
def unique_sorted(values: list) -> list:
    unique_values = sorted(set(values))
    return unique_values
