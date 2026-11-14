import unittest
from unittest.mock import patch

if __package__:
    from .app import Figure
    from .validation import count_vowels, read_positive_number
else:
    from app import Figure
    from validation import count_vowels, read_positive_number


class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Figure("квадрат", 5)

    def test_figure_type(self):
        self.assertEqual("квадрат", self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.obj.get_figure_length)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_invalid_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)


    def test_angle_counts_for_all_types(self):
        for kind, angles in [("квадрат", 4), ("прямокутник", 4), ("трикутник", 3)]:
            with self.subTest(figure_type=kind):
                self.assertEqual(angles, Figure(kind, 5).get_angles)

    def test_negative_length(self):
        with self.assertRaises(AssertionError):
            Figure("трикутник", -2)


class TestValidation(unittest.TestCase):
    @patch("builtins.input", return_value="7")
    def test_positive_input(self, mocked_input):
        self.assertEqual(7, read_positive_number())
        mocked_input.assert_called_once()

    def test_incorrect_input(self):
        for text in ("0", "-5", "abc", "1.5"):
            with self.subTest(text=text), patch("builtins.input", return_value=text):
                with self.assertRaises(ValueError):
                    read_positive_number()

    def test_vowels(self):
        cases = [("Education", 5), ("", 0), ("12345", 0), ("Україна", 4), ("Ритм", 1)]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(expected, count_vowels(text))


if __name__ == "__main__":
    unittest.main(verbosity=2)
