import random
"""Задана последовательность из 1000 целых чисел. Переставить элементы последовательности в порядке возрастания."""
def quick_sort(n):
    if len(n) <= 1:
        return n
    elem = n[0]
    left = list(filter(lambda x:x<elem, n))
    center = [i for i in n if i == elem]
    right = list(filter(lambda x:x>elem, n))

    return quick_sort(left) + center + quick_sort(right)


# a = [random.randint(2,100) for _ in range(1000)]
# print(a)
# print(quick_sort(a))

"""Написать программу, сортирующую по возрастанию одномерный массив случайных целых чисел"""
# count = random.randint(10,40)
# array = [random.randint(50,100) for _ in range(count)]
# print(array)
# print(quick_sort(array))


"""Написать программу, сортирующую по возрастанию первый столбец двумерного массива целых чисел."""
def quick_sort1(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort1(arr, low, pi - 1)
        quick_sort1(arr, pi + 1, high)


# Функция для разделения массива по опорному элементу
def partition(arr, low, high):
    pivot = arr[high][0]  # Используем первый элемент столбца как опорный
    i = low - 1
    for j in range(low, high):
        if arr[j][0] <= pivot:  # Сравниваем только первый элемент в каждой строке
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

rows = 13
cols = 7
array = [[random.randint(5, 61) for _ in range(cols)] for _ in range(rows)]

# Вывод исходного массива
# print("Исходный массив:")
# for row in array:
#     print(row)

# Сортировка массива по первому столбцу
quick_sort1(array, 0, len(array) - 1)

# Вывод отсортированного массива
# print("\nОтсортированный массив по первому столбцу:")
# for row in array:
#     print(row)


# Студенты группы
students = [
    "Ануфриев Александр Сергеевич", "Балашов Никита Андреевич", "Замашкин Антон Сергеевич", "Джибилов Давид Рустамович",
    "Зокиров Бехруз Гайратджонович", "Бекетов Назарий Александрович", "Вольф Артем Сергеевич", "Воронов Давид Анатольевич",
    "Гильманов Тимур Рустемович", "Григорьев Василий Анатольевич"
]


sorted_students = sorted(students)

# print("Отсортированный список студентов по алфавиту:")
# for student in sorted_students:
#     print(student)




