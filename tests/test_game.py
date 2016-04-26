from intro.game import Game
from nose.tools import assert_equals


class testGame():
    """
    Tests for intro.game.Game
    """

    _game = None

    def setup(self):
        self._game = Game()

    def test_roll_zero_get_zero(self):
        self._game.roll(0)
        assert_equals(self._game.score(), 0)
