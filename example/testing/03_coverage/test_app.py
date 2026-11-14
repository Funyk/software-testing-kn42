import pytest

if __package__:
    from .app import Figure
else:
    from app import Figure


@pytest.mark.parametrize(
    ("figure_type", "expected_angles"),
    [("квадрат", 4), ("прямокутник", 4), ("трикутник", 3)],
)
def test_get_angles(figure_type, expected_angles):
    assert Figure(figure_type, 1).get_angles == expected_angles


def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)


def test_unknown_type_uses_fallback():
    figure = Figure("квадрат", 1)
    figure.type = "коло"

    assert figure.get_angles == 0


def test_negative_length():
    with pytest.raises(AssertionError):
        Figure("прямокутник", -1)


def test_unknown_type():
    with pytest.raises(AssertionError):
        Figure("коло", 1)


def test_main_displays_triangle_angles(capsys):
    if __package__:
        from .app import main
    else:
        from app import main

    main()
    assert capsys.readouterr().out == "3\n"
