import collections


def find_common_in_group(groups:list) -> set:
    common:set = set(groups.pop(0))
    while groups:
        common = common.intersection(set(groups.pop(0)))
    return common


class Solution:
    def __init__(self, path:str):
        self.path = path

    def solve(self):
        f = open(self.path, "r")
        text = f.read()
        f.close()

        lines = text.split("\n")

        results = collections.deque()

        for i in range(0, len(lines), 3):
            end_index = i + 3 if i + 3 < len(lines) else len(lines)
            results.append(find_common_in_group(lines[i:end_index]))

        print(results)
        print(self.calculate_scores(results))
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