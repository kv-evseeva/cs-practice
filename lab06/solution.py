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


'''
Принимает два списка со значениями.
Возвращает список значений, которые встречаются в обоих списках
(в порядке возрастания).
'''
def common(first: list, second: list) -> list:
    common_values = sorted(set(first) & set(second))
    return common_values


'''
Принимает два списка со значениями.
Возвращает список значений из первого списка, которых нет во втором
(в порядке возрастания).
'''
def only_in_first(first: list, second: list) -> list:
    only_first = sorted(set(first) - set(second))
    return only_first


if __name__ == '__main__':
    values = ['ошибка', 'запуск', 'ошибка', 'проверка']

    print('-> Проверка на обычных значениях:')
    print(count_items(values))  # {'ошибка': 2, 'запуск': 1, 'проверка': 1}
    print(unique_sorted(values))  # ['запуск', 'ошибка', 'проверка']
    print(common(['иванов', 'петрова'], ['петрова', 'котов']))  # ['петрова']
    print(only_in_first(['иванов', 'петрова'], ['петрова', 'котов']))  # ['иванов']

    print('-> Проверка на пустых значениях:')
    print(count_items([]))
    print(unique_sorted([]))
    print(common([], []))
    print(only_in_first([], []))
