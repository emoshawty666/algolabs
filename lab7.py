def schedule_lectures(input_file="input1.txt", output_file="output1.txt"):
    """
    Составляет расписание лекций из данных во входном файле и записывает результат в выходной файл.

    Args:
        input_file: Имя входного файла, содержащего данные о заявках на лекции.
                    Формат: Первая строка - количество заявок (N).
                            Следующие N строк - по два числа в строке: si fi (время начала и окончания).
        output_file: Имя выходного файла, в который будет записано расписание лекций.
                    Формат: Каждая строка содержит si и fi через пробел для каждой запланированной лекции.
    """

    try:
        with open(input_file, "r") as f_in:
            n = int(f_in.readline().strip())
            requests = []
            for _ in range(n):
                line = f_in.readline().strip()
                s, f = map(int, line.split())
                requests.append((s, f))

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
        return
    except ValueError:
        print(f"Ошибка: Некорректный формат входных данных в файле {input_file}.")
        return
    except Exception as e:
        print(f"Ошибка: Произошла ошибка при чтении файла: {e}")
        return

    # Сортируем заявки по времени окончания в порядке возрастания.
    requests.sort(key=lambda x: x[1])

    schedule = []
    last_end_time = 0  # Время окончания последней лекции в расписании

    for start_time, end_time in requests:
        # Если лекция не пересекается с текущим расписанием, добавляем её.
        if start_time >= last_end_time:
            schedule.append((start_time, end_time))
            last_end_time = end_time

    # Сортируем расписание по времени начала (хотя это и не строго необходимо)
    schedule.sort(key=lambda x: x[0])

    try:
        with open(output_file, "w") as f_out:
            for start_time, end_time in schedule:
                f_out.write(f"{start_time} {end_time}\n")

    except Exception as e:
        print(f"Ошибка: Произошла ошибка при записи в файл: {e}")
        return


if __name__ == "__main__":
    # Запуск программы. Можно указать другие имена файлов, если необходимо.
    schedule_lectures()