from lab3.new import new_function, new_3, new_none, new_2, new_4
from lab3.main import main
from lab3.branch import fun_with_if_else, fun_with_if_only

import unittest

class TestNewFunction(unittest.TestCase):
    def test_new_function(self):
        result = new_function()
        self.assertIsInstance(result, str)
        self.assertIn("Повернене випадкове число:", result)

    def test_new_3(self):
        result = new_3()
        self.assertIsInstance(result, str)

    def test_new_none(self):
        result = new_none()
        self.assertIsNone(result)

    def test_branches_positive(self):
        i = 5
        result = fun_with_if_else(i)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Positive")

    def test_branches_zero(self):
        i = 0
        result = fun_with_if_else(i)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Zero")


    def test_if_only_branch(self):
        # перевіряємо лише гілку if x > 0
        self.assertEqual(fun_with_if_only(5), "Positive")

    def test_if_only_branch_non_positive(self):
        # перевіряємо гілку if x <= 0
        self.assertEqual(fun_with_if_only(-3), "Non-positive")
        self.assertEqual(fun_with_if_only(0), "Non-positive")

    def test_missing_new_2_and_4(self):
        # Перевіряємо, що new_2 та new_4 повертають рядки
        n2 = new_2()
        n4 = new_4()
        self.assertIsInstance(n2, str)
        self.assertIsInstance(n4, str)

    def test_branches_negative(self):
        self.assertEqual("Negative", fun_with_if_else(-5))

    def test_main_combines_results(self):
        from unittest.mock import patch

        with patch("lab3.new.random.randint", return_value=42):
            self.assertEqual(
                "Повернене випадкове число: 42Це нова функція з lab3/new.py",
                main(),
            )

    def test_handler_prints_start_and_finish(self):
        from contextlib import redirect_stdout
        from io import StringIO

        from lab3.handler import lambda_handler

        output = StringIO()
        with redirect_stdout(output):
            lambda_handler({}, None)
        self.assertEqual(
            ["Ми запустили лямбда-функцію!", "Ми завершили виконання лямбда-функції!"],
            output.getvalue().splitlines(),
        )
