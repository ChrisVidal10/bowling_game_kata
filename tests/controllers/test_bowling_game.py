import pytest
from src.controllers.game import Game

class TestBowlingGame:

    def setup_method(self):
        """
        Setup method for a Game instance.
        This instance is for each test.
        """
        self.g = Game()

    def roll_many(self, frames: int, pins: int):
        """
        Method for roll many pins in various frames.

        Args:
            frames (int): frames to play
            pins (int): Pins knock down in frames,
            the same amount of pins in every frame.
        """
        for i in range(frames):
            self.g.roll(pins)

    def test_gutter_game(self):
        """
        Test for don't knock down any pins in any frame.
        """
        self.roll_many(20, 0)
        assert 0 == self.g.score()

    def test_all_ones(self):
        """
        Test for knock down one pin in each frame
        """
        self.roll_many(20, 1)
        assert 20 == self.g.score()
    
    def test_one_spare(self):
        """
        Test for one spare in a game
        """
        self.roll_spare()
        self.g.roll(3)
        self.roll_many(17, 0)
        assert 16 == self.g.score()

    def roll_spare(self):
        """
        Spare roll method. The player knocks all 
        10 pins in two rolls.
        """
        self.g.roll(5)
        self.g.roll(5)

    def test_one_strike(self):
        """
        Test for one strike in the game.
        """
        self.roll_strike() 
        self.g.roll(3)
        self.g.roll(4)
        self.roll_many(16, 0)
        assert 24 == self.g.score()

    def roll_strike(self):
        """
        Strike roll method. The player knocks down all 
        10 pins on his first roll.
        """
        self.g.roll(10)

    def test_perfect_game(self):
        """
        Test for a perfect game. Strike roll on all frames.
        """
        self.roll_many(20, 10)
        assert 300 == self.g.score()
