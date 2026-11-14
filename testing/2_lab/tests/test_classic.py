import unittest
from unittest.mock import patch

import pytest

from lab.main import CardGame

pytestmark = pytest.mark.unit


@pytest.mark.card_combat
class TestCardGame(unittest.TestCase):
    """Це класичні unitest тести"""
    def setUp(self):
        self.game = CardGame()
        self.another_card = CardGame()

    @patch("lab.main.random.random", return_value=0.5)
    def test_hit_another_card(self, _chance):
        """Це класичні unitest тести"""
        initial_health = self.another_card.health
        self.game.hit_another_card(self.another_card)
        self.assertLess(self.another_card.health, initial_health, "Health should decrease after being hit.")

@pytest.mark.card_combat
class TestCardGameWithPytest:
    """Це pytest тести просто згруповані в клас, але без використання unittest.TestCase
    така організація дозволяє групувати тести, але pytest не потребує класів для тестів.
    """
    @patch("lab.main.random.random", return_value=0.5)
    def test_hit_another_card(self, _chance):
        """Це pytest тест"""
        game = CardGame()
        another_card = CardGame()
        initial_health = another_card.health
        game.hit_another_card(another_card)
        assert another_card.health < initial_health, "Health should decrease after being hit."
