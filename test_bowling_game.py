import unittest

from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, frame, pins):
        for x in range(frame):
            self.game.roll_ball(pins)

    def roll_spare(self):
        self.game.roll_ball(5)
        self.game.roll_ball(5)

    def roll_strike(self):
        return self.game.roll_ball(10)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.get_score())

    def test_all_ones_game(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.game.get_score())

    def test_one_spare_game(self):
        self.roll_spare()
        self.game.roll_ball(7)
        self.roll_many(17, 0)
        self.assertEqual(24, self.game.get_score())

    def test_one_strike_game(self):
        self.roll_strike()
        self.game.roll_ball(3)
        self.game.roll_ball(4)
        self.roll_many(16, 0)
        self.assertEqual(24, self.game.get_score())


if __name__ == '__main__':
    unittest.main()
