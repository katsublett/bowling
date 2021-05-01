import unittest

from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, frame, pins):
        for x in range(frame):
            self.game.roll_ball(pins)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.get_score())

    def test_all_ones_game(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.game.get_score())


if __name__ == '__main__':
    unittest.main()
