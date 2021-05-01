import unittest

from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def test_create_game(self):
        game = BowlingGame()

    def test_roll_ball(self):
        game = BowlingGame()
        game.roll_ball(5)


if __name__ == '__main__':
    unittest.main()
