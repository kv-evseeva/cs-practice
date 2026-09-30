limit = float(input("Введите порог температуры (в градусах Цельсия): "))
n = int(input("Введите количество записей: "))

err_count = 0
exceeding_count = 0
max_record, first_found = 0, False

for i in range(n):
    record = input(f"Введите {i + 1}-ю запись: ")
    if record == "error":
        err_count += 1
        continue
    record = float(record)
    if record > limit:
        exceeding_count += 1
    if not first_found:
        max_record, first_found = record, True
    if record > max_record:
        max_record = record

print("-" * 30)
print(f"Всего записей: {n}")
print(f"Количество ошибок: {err_count}")
print(f"Количество превышений порога: {exceeding_count}")
print(f"Максимальное показание: {max_record}")
