class Game():

    def __init__(self):
      self.__rolls = list()
      self.__current_roll = 0

    def roll(self, pins):
        self.__rolls.append(pins)

    def score(self):
        score = 0
        roll_index = 0
        for frame in range(10):
            if self.__rolls[roll_index]  + self.__rolls[roll_index + 1] == 10:
                score += 10 + self.__rolls[roll_index + 2]
                roll_index += 2
            else:
                score += self.__rolls[roll_index] + self.__rolls[roll_index + 1]
                roll_index += 2
        return score