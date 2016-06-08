from bowling_game.game import Game
import unittest

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.g = Game()

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEquals(0, self.g.score())

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEquals(20, self.g.score())

    def test_one_spare(self):
        self.roll_spare()
        self.g.roll(3)
        self.roll_many(17, 0)
        self.assertEquals(16, self.g.score())

    def test_roll_strike(self):
        self.roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self.assertEquals(24, self.g.score())

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEquals(300, self.g.score())

    def roll_many(self, n, pins):
        for i in range(n):
            self.g.roll(pins)

    def roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)

    def roll_strike(self):
        self.g.roll(10)
