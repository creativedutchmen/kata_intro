from intro.game import Game


def testGame():
    game = Game()
    game.roll(0)
    assert(game.score() == 1)
