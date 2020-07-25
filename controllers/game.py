class Game():

    def __init__(self):
        """
        Construct the object Game
        """
        self.__rolls = list()
        self.__current_roll = 0

    def roll(self, pins: int):
        """
        Method for a single roll.

        Args:
            pins (int): The amount of pins knocked down.
        """
        self.__rolls.append(pins)

    def score(self) -> int:
        """
        Methof for calculate the final score.

        Returns:
            int: Final score.
        """
        score = 0
        roll_index = 0
        for frame in range(10):
            if self.__is_strike(roll_index):
                score += self.__strike_bonus(roll_index)
                roll_index += 1
            elif self.__is_spare(roll_index):
                score += self.__spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self.__sum_of_rolls(roll_index)
                roll_index += 2
        return score

    def __is_spare(self, roll_index: int) -> bool:
        """
        Args:
            roll_index (int): Roll turn in a game.

        Returns:
            bools: True if is spare or false otherwise.
        """
        return self.__rolls[roll_index] + self.__rolls[roll_index + 1] == 10

    def __is_strike(self, roll_index: int) -> bool:
        """
        Args:
            roll_index (int): Roll turn in a game.

        Returns:
            bools: True if is strike or false otherwise.
        """
        return self.__rolls[roll_index] == 10

    def __strike_bonus(self, roll_index: int) -> int:
        """
        Args:
            roll_index (int): Roll turn in a game.

        Returns:
            int: The sum of a complete strike 10 + bonus in a frame.
        """
        return 10 + self.__rolls[roll_index + 1] + self.__rolls[roll_index + 2]

    def __spare_bonus(self, roll_index: int) -> int:
        """
        Args:
            roll_index (int): Roll turn in a game.

        Returns:
            int: The sum of a complete spare 10 + bonus in a frame.
        """
        return 10 + self.__rolls[roll_index + 2]

    def __sum_of_rolls(self, roll_index: int) -> int:
        """
        Args:
            roll_index (int): Roll turn in a game.

        Returns:
            int: The sum of pins knock down in a frame.
        """
        return self.__rolls[roll_index] + self.__rolls[roll_index + 1]
