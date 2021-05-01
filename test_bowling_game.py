import unittest

from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_gutter_game(self):
        for pins in range(20):
            self.game.roll_ball(0)
        self.assertEqual(0, self.game.get_score())

    def test_all_ones_game(self):
        for pins in range(20):
            self.game.roll_ball(1)
        self.assertEqual(20, self.game.get_score())


if __name__ == '__main__':
    unittest.main()
