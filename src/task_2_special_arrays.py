"""
Задание 2: Специальные массивы
Условие:
Создайте:
а) массив из пяти нулей;
б) массив из четырёх единиц;
в) последовательность чётных чисел от 2 до 12 включительно.
"""
import numpy as np


def run_task_2():
    print("=" * 50)
    print("Задание 2: Специальные массивы")
    print("=" * 50)

    # а) Массив из пяти нулей
    # np.zeros создает массив, заполненный нулями (по умолчанию float64)
    zeros_array = np.zeros(5)
    zeros_int_array = np.zeros(5, dtype=int)

    print("а) Массив из 5 нулей (float):")
    print(zeros_array)
    print("   Массив из 5 нулей (целочисленный, dtype=int):")
    print(zeros_int_array)

    # б) Массив из четырёх единиц
    # np.ones создает массив, заполненный единицами
    ones_array = np.ones(4)
    ones_int_array = np.ones(4, dtype=int)

    print("\nб) Массив из 4 единиц (float):")
    print(ones_array)
    print("   Массив из 4 единиц (целочисленный, dtype=int):")
    print(ones_int_array)

    # в) Последовательность чётных чисел от 2 до 12 включительно
    # np.arange(start, stop, step): stop не включается, поэтому указываем 13
    even_numbers = np.arange(2, 13, 2)

    print("\nв) Последовательность чётных чисел от 2 до 12 включительно:")
    print(even_numbers)
    print()

    return {
        "zeros": zeros_array,
        "zeros_int": zeros_int_array,
        "ones": ones_array,
        "ones_int": ones_int_array,
        "even_numbers": even_numbers,
    }


if __name__ == "__main__":
    run_task_2()
