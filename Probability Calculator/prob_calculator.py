import copy

import random

class Hat:
    def __init__(self, **geo):
        self.contents = []
        for color, count in geo.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents.copy()
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_draws = 0
    for _ in range(num_experiments):
        hat_copy = Hat(**{color: hat.contents.count(color) for color in hat.contents}) 
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1
        success = True
        for color, count in expected_balls.items():
            if color not in drawn_count or drawn_count[color] < count:
                success = False
                break
        if success:
            successful_draws += 1
    return successful_draws / num_experiments
