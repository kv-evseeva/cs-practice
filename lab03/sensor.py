limit = float(input("Введите порог температуры (в градусах Цельсия): "))
n = int(input("Введите количество записей: "))
err_count = 0
for i in range(n):
    record = input(f"Введите {i + 1}-ю запись: ")
    if record == "error":
        err_count += 1
print("-" * 30)
print(f"Всего записей: {n}")
print(f"Количество ошибок: {err_count}")