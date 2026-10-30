"""
Автоматические тесты для проверки корректности выполнения всех заданий.
Запуск:
    python -m unittest tests/test_tasks.py
"""
import unittest
import numpy as np
from src.task_1_create_array import run_task_1
from src.task_2_special_arrays import run_task_2
from src.task_3_array_properties import run_task_3
from src.task_4_indexing import run_task_4
from src.task_5_slicing import run_task_5
from src.task_6_2d_array import run_task_6


class TestNumPyTasks(unittest.TestCase):

    def test_task_1_create_array(self):
        """Проверка Задания 1: массив [5, 10, 15, 20, 25]"""
        values = run_task_1()
        expected = np.array([5, 10, 15, 20, 25])
        np.testing.assert_array_equal(values, expected)
        self.assertEqual(len(values), 5)

    def test_task_2_special_arrays(self):
        """Проверка Задания 2: zeros(5), ones(4), arange(2, 14, 2)"""
        res = run_task_2()
        np.testing.assert_array_equal(res["zeros"], np.zeros(5))
        self.assertEqual(len(res["zeros"]), 5)

        np.testing.assert_array_equal(res["ones"], np.ones(4))
        self.assertEqual(len(res["ones"]), 4)

        expected_even = np.array([2, 4, 6, 8, 10, 12])
        np.testing.assert_array_equal(res["even_numbers"], expected_even)

    def test_task_3_array_properties(self):
        """Проверка Задания 3: ndim, shape, size, dtype"""
        a, theory = run_task_3()
        self.assertEqual(a.ndim, 2)
        self.assertEqual(a.shape, (2, 3))
        self.assertEqual(a.size, 6)
        self.assertTrue(np.issubdtype(a.dtype, np.integer))

    def test_task_4_indexing(self):
        """Проверка Задания 4: первый, третий, последний и замена 30 -> 100"""
        res = run_task_4()
        self.assertEqual(res["first"], 10)
        self.assertEqual(res["third"], 30)
        self.assertEqual(res["last"], 50)
        np.testing.assert_array_equal(
            res["modified_array"],
            np.array([10, 20, 100, 40, 50])
        )

    def test_task_5_slicing(self):
        """Проверка Задания 5: срезы массива numbers"""
        res = run_task_5()
        # элементы с индексами 1, 2, 3
        np.testing.assert_array_equal(res["slice_1_to_3"], np.array([20, 30, 40]))
        # первые 3 элемента
        np.testing.assert_array_equal(res["first_three"], np.array([10, 20, 30]))
        # начиная с индекса 2
        np.testing.assert_array_equal(res["from_index_2"], np.array([30, 40, 50]))

    def test_task_6_2d_array(self):
        """Проверка Задания 6: оценка 88, 2-я строка, 3-й столбец"""
        res = run_task_6()
        self.assertEqual(res["grade_88"], 88)
        np.testing.assert_array_equal(res["second_row"], np.array([70, 88, 92]))
        np.testing.assert_array_equal(res["third_column"], np.array([78, 92, 89]))


if __name__ == "__main__":
    unittest.main()
