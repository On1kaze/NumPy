"""
Задание 4: Индексы
Условие:
Дан массив numbers. Выведите первый, третий и последний элементы.
После этого замените число 30 на 100.

numbers = np.array([10, 20, 30, 40, 50])
"""
import numpy as np


def run_task_4():
    print("=" * 50)
    print("Задание 4: Индексы")
    print("=" * 50)

    # Исходный массив
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"Исходный массив numbers: {numbers}")

    # В Python индексация начинается с 0:
    # Индексы:   0   1   2   3   4
    # Значения: 10, 20, 30, 40, 50
    # Отриц.:  -5  -4  -3  -2  -1

    first_elem = numbers[0]     # Первый элемент (индекс 0)
    third_elem = numbers[2]     # Третий элемент (индекс 2)
    last_elem = numbers[-1]     # Последний элемент (индекс -1 или len(numbers) - 1)

    print(f"• Первый элемент (индекс 0):    {first_elem}")
    print(f"• Третий элемент (индекс 2):    {third_elem}")
    print(f"• Последний элемент (индекс -1): {last_elem}")

    # Замена числа 30 на 100
    # Способ 1: по индексу (число 30 имеет индекс 2)
    numbers[2] = 100
    print(f"\nМассив после замены числа 30 на 100 (по индексу [2]):")
    print(numbers)

    # Дополнительно: демонстрация универсальной замены по условию
    # (если позиция числа заранее неизвестна):
    # numbers[numbers == 30] = 100
    print()

    return {
        "first": first_elem,
        "third": third_elem,
        "last": last_elem,
        "modified_array": numbers,
    }


if __name__ == "__main__":
    run_task_4()
