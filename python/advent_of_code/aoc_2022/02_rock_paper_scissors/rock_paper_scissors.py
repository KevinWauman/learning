import collections

class Solution:
    """
    A, X -> Rock 1
    B, Y -> Paper 2
    C, Z -> Scissors 3
    """

    WIN = 6
    DRAW = 3
    LOSE = 0

    points_for_choice = {
        "A" : 1, "X" : 1,
        "B" : 2, "Y" : 2,
        "C" : 3, "Z" : 3
    }

    def __init__(self, path:str):
        self.path = path

    def rock_paper_scissors(self):
        f = open(path, 'r')
        text = f.read()
        f.close()
        all_games = [_.split(" ") for _ in text.split("\n")]
        results = collections.deque()

        for _ in all_games:
            results.append(self._score(_[0], _[1]))

        return results

    def my_points(self):
        return sum([b for a,b in self.rock_paper_scissors()])

    def _score(self, opponent_play, my_play):
        my_points = self.points_for_choice.get(my_play)
        opponent_points = self.points_for_choice.get(opponent_play)

        if my_points == opponent_points:
            return opponent_points + self.DRAW, my_points + self.DRAW

        if my_points - 1 % 3 == opponent_points % 3:
            return  opponent_points + self.LOSE, my_points + self.WIN
        else:
            return  opponent_points + self.WIN, my_points + self.LOSE


class SolutionPart2:
    """
    A -> Rock 1
    B -> Paper 2
    C -> Scissors 3

    X -> Lose
    Y -> Draw
    Z -> Win
    """

    WIN = 6
    DRAW = 3
    LOSE = 0

    points_for_choice = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    strategy = {
        "X": -1,
        "Y": 0,
        "Z": 1
    }

    def __init__(self, path: str):
        self.path = path

    def rock_paper_scissors(self):
        f = open(self.path, 'r')
        text = f.read()
        f.close()
        all_games = [_.split(" ") for _ in text.split("\n")]
        results = collections.deque()

        for _ in all_games:
            results.append(self._score(_[0], _[1]))

        return results

    def my_points(self):
        return sum([b for a, b in self.rock_paper_scissors()])

    def _score(self, opponent_play, my_strat):
        opponent_points = self.points_for_choice.get(opponent_play)
        my_points = (self.strategy.get(my_strat) + opponent_points - 1) % 3 + 1

        if my_points == opponent_points:
            return opponent_points + self.DRAW, my_points + self.DRAW

        if my_points - 1 % 3 == opponent_points % 3:
            return opponent_points + self.LOSE, my_points + self.WIN
        else:
            return opponent_points + self.WIN, my_points + self.LOSE



# path = "input.txt"
# s = Solution(path)
#
# print(s.my_points())

path_p2 = "input_2.txt"
s2 = SolutionPart2(path_p2)
print(s2.my_points())