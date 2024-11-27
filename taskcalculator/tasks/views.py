from django.shortcuts import render
from .models import TaskInput
from .forms import TaskInputForm
from .utils import calculate_costs_with_check
from django.shortcuts import render, get_object_or_404
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from .models import TaskInput


def generate_gantt_chart(request, pk):
    """
    Генерация диаграммы Ганта для задачи по ID и возврат изображения через HttpResponse.
    """
    # Получаем задачу по ID
    task = get_object_or_404(TaskInput, id=pk)
    
    # Парсим данные из текстового поля
    tasks = parse_input_data(task.raw_data)
    
    # Вычисление времени начала каждой задачи с учетом зависимостей
    for task_item in tasks:
        if task_item["start"] == 0:
            task_item["start_time"] = 0  # Задачи, начинающиеся с 0, начинают с 0
        else:
            # Задача начинается после завершения всех зависимых задач
            prev_tasks = [t for t in tasks if t["end"] == task_item["start"]]
            task_item["start_time"] = max([t["start_time"] + t["T"] for t in prev_tasks])

    # Устанавливаем время завершения для каждой задачи
    for task_item in tasks:
        task_item["end_time"] = task_item["start_time"] + task_item["T"]

    # Создаём Gantt chart
    fig, ax = plt.subplots(figsize=(10, 6))

    for task_item in tasks:
        start_time = task_item["start_time"]
        duration = task_item["T"]
        label = f"{task_item['start']}-{task_item['end']}"
        ax.barh(label, duration, left=start_time, color="skyblue", edgecolor="black")
        ax.text(start_time + duration / 2, tasks.index(task_item), str(duration), 
                va='center', ha='center', fontsize=9)

    # Настройка осей
    ax.set_xlabel("Время выполнения работ")
    ax.set_ylabel("Работы")
    ax.set_title(f"Диаграмма Ганта для задачи {pk}")
    ax.grid(True, axis="x", linestyle="--", alpha=0.7)

    # Сохраняем график в буфер
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close(fig)
    
    # Возвращаем изображение как HTTP-ответ
    return HttpResponse(buffer, content_type='image/png')


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
