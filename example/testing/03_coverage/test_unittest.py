import unittest

if __package__:
    from .app import Figure
else:
    from app import Figure


class TestFigure(unittest.TestCase):
    def test_square_has_four_angles(self):
        self.assertEqual(4, Figure("квадрат", 1).get_angles)

    def test_rectangle_has_four_angles(self):
        self.assertEqual(4, Figure("прямокутник", 1).get_angles)

    def test_triangle_has_three_angles(self):
        self.assertEqual(3, Figure("трикутник", 1).get_angles)

    def test_unknown_type_uses_fallback(self):
        figure = Figure("квадрат", 1)
        figure.type = "коло"

        self.assertEqual(0, figure.get_angles)

    def test_invalid_length_raises_assertion_error(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    def test_invalid_type_raises_assertion_error(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)


class TestProgram(unittest.TestCase):
    def test_main_displays_triangle_angles(self):
        from contextlib import redirect_stdout
        from io import StringIO

        if __package__:
            from .app import main
        else:
            from app import main

        output = StringIO()
        with redirect_stdout(output):
            main()
        self.assertEqual("3\n", output.getvalue())


if __name__ == "__main__":
    unittest.main()
