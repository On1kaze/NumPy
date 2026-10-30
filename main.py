"""
Практическая работа по основам программирования на Python (NumPy)
================================================================
Основной скрипт для запуска всех 6 заданий практической работы.

Содержание:
- Задание 1: Создание массива (values)
- Задание 2: Специальные массивы (zeros, ones, arange)
- Задание 3: Свойства массива (ndim, shape, size, dtype)
- Задание 4: Индексы (доступ по индексу и замена элемента)
- Задание 5: Срезы (срезы по индексам, первые N, срез до конца)
- Задание 6: Двумерный массив (доступ к элементу, строке, столбцу)
"""
import sys
from src.task_1_create_array import run_task_1
from src.task_2_special_arrays import run_task_2
from src.task_3_array_properties import run_task_3
from src.task_4_indexing import run_task_4
from src.task_5_slicing import run_task_5
from src.task_6_2d_array import run_task_6


def main():
    print("#" * 60)
    print("  ПРАКТИЧЕСКАЯ РАБОТА: ОСНОВЫ ПРОГРАММИРОВАНИЯ НА PYTHON (NUMPY)")
    print("#" * 60)
    print()

    run_task_1()
    run_task_2()
    run_task_3()
    run_task_4()
    run_task_5()
    run_task_6()

    print("#" * 60)
    print("  ВСЕ ЗАДАНИЯ УСПЕШНО ВЫПОЛНЕНЫ!")
    print("#" * 60)


if __name__ == "__main__":
    main()
