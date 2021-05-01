import unittest

from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def test_create_game(self):
        game = BowlingGame()

    def test_roll_ball(self):
        game = BowlingGame()
        game.roll_ball(5)

    def test_gutter_game(self):
        game = BowlingGame()
        for pins in range(20):
            game.roll_ball(0)
        self.assertEqual(0, game.get_score())


if __name__ == '__main__':
    unittest.main()
