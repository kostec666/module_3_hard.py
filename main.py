def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, (list, tuple, set)):
        for element in data:
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Суммируем ключи
            total_sum += calculate_structure_sum(value)  # Суммируем значения
    elif isinstance(data, str):
        total_sum += len(data)  # Добавляем длину строки
    elif isinstance(data, (int, float)):  # Проверяем на числа
        total_sum += data

    return total_sum

# Применение функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99