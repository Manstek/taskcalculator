# Исходные данные
# """Тест 2."""
# tasks = [
#     {"start": 0, "end": 1, "Tmin": 2, "Tmax": 5, "Cmin": 1, "Cmax": 6, "Cmin_kosv": 3, "Cmax_kosv": 8, "T": 2},
#     {"start": 0, "end": 2, "Tmin": 3, "Tmax": 5, "Cmin": 2, "Cmax": 7, "Cmin_kosv": 4, "Cmax_kosv": 7, "T": 3},
#     {"start": 1, "end": 4, "Tmin": 3, "Tmax": 6, "Cmin": 2, "Cmax": 7, "Cmin_kosv": 4, "Cmax_kosv": 7, "T": 3},
#     {"start": 2, "end": 3, "Tmin": 2, "Tmax": 6, "Cmin": 3, "Cmax": 5, "Cmin_kosv": 4, "Cmax_kosv": 5, "T": 6},
#     {"start": 2, "end": 4, "Tmin": 2, "Tmax": 4, "Cmin": 1, "Cmax": 5, "Cmin_kosv": 3, "Cmax_kosv": 7, "T": 2},
#     {"start": 3, "end": 4, "Tmin": 1, "Tmax": 5, "Cmin": 1, "Cmax": 6, "Cmin_kosv": 3, "Cmax_kosv": 6, "T": 1},
# ]


# """Тест 1."""
# tasks = [
#     {"start": 0, "end": 1, "Tmin": 3, "Tmax": 5, "Cmin": 3, "Cmax": 4, "Cmin_kosv": 3, "Cmax_kosv": 4, "T": 3},
#     {"start": 0, "end": 2, "Tmin": 3, "Tmax": 4, "Cmin": 2, "Cmax": 4, "Cmin_kosv": 2, "Cmax_kosv": 4, "T": 4},
#     {"start": 1, "end": 2, "Tmin": 3, "Tmax": 4, "Cmin": 4, "Cmax": 5, "Cmin_kosv": 4, "Cmax_kosv": 6, "T": 3},
#     {"start": 1, "end": 3, "Tmin": 6, "Tmax": 7, "Cmin": 5, "Cmax": 6, "Cmin_kosv": 5, "Cmax_kosv": 6, "T": 7},
#     {"start": 2, "end": 3, "Tmin": 4, "Tmax": 5, "Cmin": 6, "Cmax": 7, "Cmin_kosv": 6, "Cmax_kosv": 7, "T": 4},
# ]


"""Тест 3."""
tasks = [
    {"start": 0, "end": 1, "Tmin": 10, "Tmax": 20, "Cmin": 3, "Cmax": 10, "Cmin_kosv": 3, "Cmax_kosv": 15, "T": 10},
    {"start": 0, "end": 2, "Tmin": 12, "Tmax": 32, "Cmin": 3, "Cmax": 10, "Cmin_kosv": 3, "Cmax_kosv": 15, "T": 12},
    {"start": 1, "end": 2, "Tmin": 2, "Tmax": 12, "Cmin": 2, "Cmax": 10, "Cmin_kosv": 2, "Cmax_kosv": 15, "T": 2},
    {"start": 1, "end": 3, "Tmin": 2, "Tmax": 7, "Cmin": 6, "Cmax": 10, "Cmin_kosv": 4, "Cmax_kosv": 15, "T": 2},
    {"start": 2, "end": 7, "Tmin": 2, "Tmax": 7, "Cmin": 10, "Cmax": 20, "Cmin_kosv": 7, "Cmax_kosv": 25, "T": 2},
    {"start": 3, "end": 4, "Tmin": 16, "Tmax": 26, "Cmin": 20, "Cmax": 30, "Cmin_kosv": 15, "Cmax_kosv": 35, "T": 16},
    {"start": 3, "end": 5, "Tmin": 8, "Tmax": 13, "Cmin": 10, "Cmax": 20, "Cmin_kosv": 8, "Cmax_kosv": 25, "T": 8},
    {"start": 4, "end": 6, "Tmin": 12, "Tmax": 22, "Cmin": 30, "Cmax": 40, "Cmin_kosv": 20, "Cmax_kosv": 45, "T": 12},
    {"start": 5, "end": 6, "Tmin": 20, "Tmax": 25, "Cmin": 40, "Cmax": 50, "Cmin_kosv": 24, "Cmax_kosv": 55, "T": 20},
    {"start": 6, "end": 7, "Tmin": 8, "Tmax": 13, "Cmin": 15, "Cmax": 22, "Cmin_kosv": 12, "Cmax_kosv": 27, "T": 8},
    {"start": 7, "end": 8, "Tmin": 6, "Tmax": 11, "Cmin": 3, "Cmax": 11, "Cmin_kosv": 3, "Cmax_kosv": 16, "T": 6},
]



# Функция для расчёта затрат
def calculate_costs(tasks):
    print(tasks)
    total_Cpr = 0
    total_Ckos = 0
    results = []

    for task in tasks:
        Tmin, Tmax = task["Tmin"], task["Tmax"]
        Cmin, Cmax = task["Cmin"], task["Cmax"]
        Cmin_kosv, Cmax_kosv = task["Cmin_kosv"], task["Cmax_kosv"]
        T = task["T"]

        # Расчёт прямых затрат
        Cpr = Cmin + (Cmax - Cmin) / (Tmax - Tmin) * (Tmax - T)

        # Расчёт косвенных затрат
        Ckos = Cmin_kosv + (Cmax_kosv - Cmin_kosv) / (Tmax - Tmin) * (T - Tmin)

        # Добавление в результат
        results.append({"T": T, "Cpr": round(Cpr, 2), "Ckos": round(Ckos, 2)})

        # Суммирование
        total_Cpr += Cpr
        total_Ckos += Ckos

    return results, round(total_Cpr, 2), round(total_Ckos, 2)

# Расчёт затрат
results, total_Cpr, total_Ckos = calculate_costs(tasks)

# Вывод результатов
print("T  Cпр  Скос")
for res in results:
    print(f"{res['T']}  {res['Cpr']}  {res['Ckos']}")

print(f"\nСумма прямых затрат: {total_Cpr}")
print(f"Сумма косвенных затрат: {total_Ckos}")
print(f"Суммарные затраты: {total_Cpr + total_Ckos}")
