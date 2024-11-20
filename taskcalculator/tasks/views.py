from django.shortcuts import render
from .models import TaskInput
from .forms import TaskInputForm
from .utils import calculate_costs_with_check
from django.shortcuts import render, get_object_or_404

def parse_input_data(raw_data):
    tasks = []
    rows = raw_data.strip().split("\n")
    for row in rows:
        values = list(map(int, row.split()))
        task = {
            "start": values[0],
            "end": values[1],
            "Tmin": values[2],
            "Tmax": values[3],
            "Cmin": values[4],
            "Cmax": values[5],
            "Cmin_kosv": values[6],
            "Cmax_kosv": values[7],
            "T": values[8]
        }
        tasks.append(task)
    return tasks

def task_input_view(request):
    if request.method == 'POST':
        form = TaskInputForm(request.POST)
        if form.is_valid():
            task_input = form.save()
            tasks = parse_input_data(task_input.raw_data)
            # Вы можете здесь вызвать функцию calculate_costs_with_check и передать данные `tasks`.

            calc = calculate_costs_with_check(tasks, task_input.td)
            return render(request, 'tasks/result.html', {'tasks': tasks, 'calc': calc}, )
    else:
        form = TaskInputForm()
    return render(request, 'tasks/input.html', {'form': form})



def view_task(request, pk):
    # Получение записи из базы данных по ID
    task = get_object_or_404(TaskInput, id=pk)
    print(f"Viewing task with ID: {pk}")
    
    # Парсинг данных из текстового поля
    tasks = []
    for line in task.raw_data.splitlines():  # Используем raw_data
        if line.strip():  # Если строка не пустая
            # Разделение строки на части и преобразование в целые числа
            start, end, Tmin, Tmax, Cmin, Cmax, Cmin_kosv, Cmax_kosv, T = map(int, line.split())
            tasks.append({
                "start": start,
                "end": end,
                "Tmin": Tmin,
                "Tmax": Tmax,
                "Cmin": Cmin,
                "Cmax": Cmax,
                "Cmin_kosv": Cmin_kosv,
                "Cmax_kosv": Cmax_kosv,
                "T": T
            })

    # Передаем задачи и ID задачи в шаблон
    calc = calculate_costs_with_check(tasks, task.td)
    return render(request, 'tasks/view_task.html', {'tasks': tasks, 'task_id': task.pk, 'calc': calc})
