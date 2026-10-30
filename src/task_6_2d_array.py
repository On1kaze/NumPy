"""
Задание 6: Двумерный массив
Условие:
Для матрицы grades выведите оценку 88, всю вторую строку и весь третий столбец.

grades = np.array([[85, 90, 78],
                   [70, 88, 92],
                   [95, 81, 89]])
"""
import numpy as np


def run_task_6():
    print("=" * 50)
    print("Задание 6: Двумерный массив")
    print("=" * 50)

    # Исходная матрица
    grades = np.array([[85, 90, 78],
                       [70, 88, 92],
                       [95, 81, 89]])

    print("Матрица оценок grades:")
    print(grades)
    print()

    # 1. Вывод оценки 88
    # Оценка 88 находится во 2-й строке (индекс 1) и во 2-м столбце (индекс 1)
    grade_88 = grades[1, 1]
    print(f"• Оценка 88 (строка 1, столбец 1): {grade_88}")

    # 2. Вся вторая строка
    # Вторая по счёту строка имеет индекс 1: grades[1] или grades[1, :]
    second_row = grades[1]
    print(f"• Вся вторая строка grades[1]:     {second_row}")

    # 3. Весь третий столбец
    # Третий по счёту столбец имеет индекс 2: grades[:, 2]
    third_column = grades[:, 2]
    print(f"• Весь третий столбец grades[:, 2]: {third_column}")
    print()

    return {
        "grade_88": grade_88,
        "second_row": second_row,
        "third_column": third_column,
    }


if __name__ == "__main__":
    run_task_6()
