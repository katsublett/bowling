class BowlingGame:
    def __init__(self):
        self.rolls = [0] * 21
        self.current_roll = 0

    def roll_ball(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def is_spare(self, first_ball_in_frame):
        return self.rolls[first_ball_in_frame] + self.rolls[first_ball_in_frame + 1] == 10

    def get_score(self):
        score = 0
        first_ball_in_frame = 0

        for frame in range(0, 10):
            if self.is_spare(first_ball_in_frame):
                score += 10 + self.rolls[first_ball_in_frame + 2]
                first_ball_in_frame += 2
            else:
                score += self.rolls[first_ball_in_frame] + \
                    self.rolls[first_ball_in_frame + 1]
                first_ball_in_frame += 2

        return score
