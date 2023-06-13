class Solution:

    def __init__(self, input_path):
        self.input_path = input_path

    def solve(self):
        f = open(self.input_path, "r")
        text = f.read()
        f.close()
        top3 = [-1] * 3
        grouped_int = [[int(_) for _ in i.split("\n")] for i in text.split("\n\n")]
        tree = Heap()
        for _ in grouped_int:
            tree.append(sum(_))
        return [tree.pop() for _ in range(3)]

class Heap:
    def __init__(self):
        self.heap = []

    def append(self, value):
        self.heap.append(value)
        index_self = len(self.heap) - 1
        index_parent = index_self // 2
        while True:
            if index_parent == index_self:
                break
            if self.heap[index_parent] < self.heap[index_self]:
                self.heap[index_parent], self.heap[index_self] = self.heap[index_self], self.heap[index_parent]
                index_self = index_parent
                index_parent = index_self // 2
            else: break

    def pop(self) -> int:
        value = self.heap[0]
        self.heap[0] = self.heap.pop(len(self.heap) - 1)
        self.sort(0)
        return value

    def sort(self, index):
        value = self.heap[index]
        index_l = index * 2
        index_r = index_l + 1
        value_l = self.heap[index_l] if index_l < len(self.heap) else None
        value_r = self.heap[index_r] if index_r < len(self.heap) else None

        if value_r and value_r > value_l and value_r > value:
            self._switch(index, index_r)
            self.sort(index_r)
        elif value_l and value_l > value_r and value_l > value:
            self._switch(index, index_l)
            self.sort(index_l)

    def _switch(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

s = Solution("input_top3.txt")
print(sum(s.solve()))