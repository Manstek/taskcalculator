def calculate_costs_with_check(tasks, td=10000):
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
