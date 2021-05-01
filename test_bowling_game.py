import unittest

from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def test_create_game(self):
        game = BowlingGame()


if __name__ == '__main__':
    unittest.main()
