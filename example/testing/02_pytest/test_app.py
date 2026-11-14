import pytest

if __package__:
    from .app import Figure
else:
    from app import Figure


@pytest.fixture
def square():
    return Figure("квадрат", 10)


@pytest.fixture(scope="module")
def allowed_figures():
    return tuple(Figure.FIGURES)


@pytest.mark.unit
def test_triangle_type():
    assert Figure("трикутник", 4).type == "трикутник"


@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type):
    assert Figure(figure_type, 1).type == figure_type


@pytest.mark.unit
def test_square_length(square):
    assert square.get_figure_length == 10


def test_invalid_figure():
    with pytest.raises(AssertionError):
        Figure("коло", 1)


@pytest.mark.parametrize("kind", ["коло", "", None])
def test_disallowed_types(kind):
    with pytest.raises(AssertionError, match="Невідомий тип"):
        Figure(kind, 1)


@pytest.mark.parametrize("length", [0, -1, -10])
def test_invalid_lengths(length):
    with pytest.raises(AssertionError, match="Довжина"):
        Figure("квадрат", length)


@pytest.mark.parametrize("length", ["3", None, []])
def test_non_numeric_lengths(length):
    with pytest.raises(TypeError):
        Figure("квадрат", length)


def test_fixture_contains_three_figures(allowed_figures):
    assert len(allowed_figures) == 3


def test_fixture_contains_rectangle(allowed_figures):
    assert "прямокутник" in allowed_figures
