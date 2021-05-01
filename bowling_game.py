class BowlingGame:
    def __init__(self):
        self.frame = [0] * 21
        self.current_roll = 0

    def roll_ball(self, pins):
        self.frame[self.current_roll] = pins
        self.current_roll += 1

    def is_spare(self, first_ball):
        return self.frame[first_ball] + self.frame[first_ball + 1] == 10

    def is_strike(self, first_ball):
        return self.frame[first_ball] == 10

    def spare_bonus(self, first_ball):
        return self.frame[first_ball + 2]

    def strike_bonus(self, first_ball):
        return self.frame[first_ball + 1] + self.frame[first_ball + 2]

    def frame_score(self, first_ball):
        return self.frame[first_ball] + self.frame[first_ball + 1]

    def get_score(self):
        score = 0
        first_ball = 0

        for frame in range(0, 10):
            if self.is_strike(first_ball):
                score += 10 + self.strike_bonus(first_ball)
                first_ball += 1
            if self.is_spare(first_ball):
                score += 10 + self.spare_bonus(first_ball)
                first_ball += 2
            else:
                score += self.frame_score(first_ball)
                first_ball += 2

        return score
