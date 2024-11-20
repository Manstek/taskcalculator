
def calculate_costs_with_check(tasks, td):
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

        # Вычисление директивного времени (среднее значение между Tmin и Tmax)
        T_directive = (Tmin + Tmax) / 2

        # Добавление в результат
        results.append({
            "T": T, 
            "Cpr": round(Cpr, 2), 
            "Ckos": round(Ckos, 2), 
            "T_directive": round(T_directive, 2)
        })

        # Суммирование
        total_Cpr += Cpr
        total_Ckos += Ckos

    if check_feasibility(tasks, results, td):
        return results, round(total_Cpr, 2), round(total_Ckos, 2)
    else:
        return "Задачи не могут быть выполнены в пределах заданного директивного времени."


def check_feasibility(tasks, results, td):
    end_times = {0: 0}  # Время завершения для каждой вершины, стартуем с вершины 0
    for task, result in zip(tasks, results):
        start_time = end_times.get(task["start"], 0)
        end_time = start_time + result["T"]
        if end_time > td:
            return False  # Нарушение директивного времени
        end_times[task["end"]] = max(end_times.get(task["end"], 0), end_time)
    return True
