import collections

class Solution:
    def __init__(self, path:str):
        self.path = path

    def solve(self):
        f = open(self.path, "r")
        text = f.read()
        f.close()

        lines = text.split("\n")

        results = collections.deque()

        for line in lines:
            a = line[0: len(line) // 2]
            b = line[len(line) // 2:]

            chars_a = set([_ for _ in a])
            chars_b = set([_ for _ in b])

            results.append(chars_a.intersection(chars_b))

        return sum(self.calculate_scores(results))

    def calculate_scores(self, iterable) -> collections.deque:
        new_list = collections.deque()
        for _ in iterable:
            sum = 0
            for i in _:
                if ord(i) > ord("a") - 1:
                    sum += ord(i) - (ord("a") - 1)
                else:
                    sum += ord(i) - (ord("A") - 1) + 26
            new_list.append(sum)
        return new_list



path = "input.txt"
s = Solution(path)
print(s.solve())

# print(ord('a'))
# print(ord('A'))