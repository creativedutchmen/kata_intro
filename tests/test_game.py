from intro.game import Game, Rule
from nose.tools import assert_equals, raises


class testGame():
    """
    Tests for intro.game.Game
    """

    _game = None

    def setup(self):
        self._game = Game()

    def test_start_zero(self):
        assert_equals(self._game.score(), 0)

    def test_gutter_game(self):
        self._throw_multiple(n=10, frame=(0, 0))
        assert_equals(self._game.score(), 0)

    def test_ones_game(self):
        self._throw_multiple(n=10, frame=(1, 1))
        assert_equals(self._game.score(), 20)

    def test_spare(self):
        self._game.add_frame((5, 5))
        self._game.add_frame((7, 1))
        assert_equals(self._game.score(), 17+8)

    def test_strike(self):
        self._game.add_frame((10, 0))
        self._game.add_frame((1, 1))
        assert_equals(self._game.score(), 14)

    def test_last_throw_spare(self):
        self._throw_multiple(n=9, frame=(0, 0))
        self._game.add_frame((5, 5, 5))
        assert_equals(self._game.score(), 15)

    def test_last_throw_spare_gutter(self):
        self._throw_multiple(n=9, frame=(0, 0))
        self._game.add_frame((5, 5, 0))
        assert_equals(self._game.score(), 10)

    def test_last_throw_strike(self):
        self._throw_multiple(n=9, frame=(0, 0))
        self._game.add_frame((10, 5, 5))
        assert_equals(self._game.score(), 20)

    def test_perfect_game(self):
        self._throw_multiple(n=9, frame=(10, 0))
        self._game.add_frame((10, 10, 10))
        assert_equals(self._game.score(), 300)

    """
    Test negative paths
    """
    @raises(ValueError)
    def test_long_game(self):
        self._throw_multiple(n=11, frame=(1, 1))

    @raises(ValueError)
    def test_many_pins(self):
        self._game.add_frame((11, 0))

    @raises(ValueError)
    def test_three_throws(self):
        self._game.add_frame((10, 10, 10))

    @raises(ValueError)
    def test_three_throws_without_spare_or_strike(self):
        self._throw_multiple(n=9, frame=(1, 1))
        self._game.add_frame((1, 1, 1))

    @raises(ValueError)
    def test_negative_score(self):
        self._game.add_frame((-1, 1))

    @raises(ValueError)
    def test_two_lanes(self):
        self._game.add_frame((10, 5))

    def invalid_input_is_not_saved(self):
        try:
            self._game.add_frame((10, 5))
        except ValueError:
            assert_equals(self._game.score(), 0)

    """
    Testing the fun part: adding new rules on the fly
    """
    def test_add_rule_before(self):
        self._throw_multiple(n=3, frame=(10, 0))

    @raises(Exception)
    def test_add_rule_after(self):
        # Note I am writing to a variable I should not be writing to.
        # It would be cleaner to extend the Game class and add it to the
        # __init__ function. However, for the test this is fine.
        self._game._rules.append(ThreeStrikesOut())
        self._throw_multiple(n=3, frame=(10, 0))

    """
    Helpers
    """
    def _throw_multiple(self, n, frame):
        for i in range(0, n):
            self._game.add_frame(frame)


class ThreeStrikesOut(Rule):
    """
    Testing the ability to add new rules
    """
    def is_valid(self, frames):
        strikes = 0
        for frame in frames:
            if frame[0] == 10:
                strikes += 1
        if strikes >= 3:
            raise Exception('You\'re out!')

    def calculate_score(self, frames):
        pass
