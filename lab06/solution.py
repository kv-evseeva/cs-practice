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
