def process_numbers(input_numbers):
    current_set = set()

    for number in input_numbers:
        if number > 0:
            current_set.add(number)
        elif number < 0:
            current_set.discard(-number)
        elif number == 0:
            return sorted(current_set)

    return sorted(current_set)


# Чтение входных данных из файла
with open('input.txt', 'r') as file:
    numbers = list(map(int, file.read().strip().split()))

# Обработка чисел
result = process_numbers(numbers)

# Запись результата в выходной файл
with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, result)))


