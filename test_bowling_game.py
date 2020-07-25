import pytest
from controllers.game import Game

class TestBowlingGame:

    def seutp_class(self):
        print("Acá todo comienza")

    def setup_method(self):
        self.g = Game()

    def roll_many(self, frames, pins):
        for i in range(frames):
            self.g.roll(pins)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        assert 0 == self.g.score()

    def test_all_ones(self):
        self.roll_many(20, 1)
        assert 20 == self.g.score()

    def test_one_spare(self):
        self.g.roll(5)
        self.g.roll(5) #spare
        self.g.roll(3)
        self.roll_many(17, 0)
        assert 16 == self.g.score()