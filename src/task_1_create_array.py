"""
Задание 1: Создание массива
Условие:
Создайте массив values из чисел 5, 10, 15, 20 и 25. Выведите массив на экран.
"""
import numpy as np


def run_task_1():
    print("=" * 50)
    print("Задание 1: Создание массива")
    print("=" * 50)

    # Создание одномерного массива из списка чисел
    values = np.array([5, 10, 15, 20, 25])

    # Вывод массива и его типа на экран
    print("Созданный массив values:")
    print(values)
    print(f"Тип объекта: {type(values)}")
    print(f"Тип элементов массива: {values.dtype}")
    print()

    return values


if __name__ == "__main__":
    run_task_1()
