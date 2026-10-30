"""
Задание 5: Срезы
Условие:
Из массива numbers получите:
а) элементы с индексами от 1 до 3;
б) первые три элемента;
в) элементы начиная с индекса 2.

numbers = np.array([10, 20, 30, 40, 50])
"""
import numpy as np


def run_task_5():
    print("=" * 50)
    print("Задание 5: Срезы")
    print("=" * 50)

    # Исходный массив
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"Исходный массив numbers: {numbers}")
    print("Индексы элементов:       [ 0   1   2   3   4 ]\n")

    # а) Элементы с индексами от 1 до 3
    # В Python правая граница среза [start:stop] не включается.
    # Если требуются индексы 1, 2 и 3 включительно, срез: numbers[1:4]
    slice_1_to_3_inclusive = numbers[1:4]
    # Если срез понимается буквально как range(1, 3): numbers[1:3]
    slice_1_to_3_exclusive = numbers[1:3]

    print("а) Элементы с индексами от 1 до 3:")
    print(f"   numbers[1:4] (индексы 1, 2, 3): {slice_1_to_3_inclusive}")
    print(f"   numbers[1:3] (индексы 1, 2):    {slice_1_to_3_exclusive}")

    # б) Первые три элемента (индексы 0, 1, 2)
    # Срез [:3] эквивалентен [0:3]
    first_three = numbers[:3]
    print(f"\nб) Первые три элемента numbers[:3]:")
    print(f"   {first_three}")

    # в) Элементы начиная с индекса 2
    # Срез [2:] берет элементы от индекса 2 до конца массива
    from_index_2 = numbers[2:]
    print(f"\nв) Элементы начиная с индекса 2 numbers[2:]:")
    print(f"   {from_index_2}")
    print()

    return {
        "slice_1_to_3": slice_1_to_3_inclusive,
        "first_three": first_three,
        "from_index_2": from_index_2,
    }


if __name__ == "__main__":
    run_task_5()
