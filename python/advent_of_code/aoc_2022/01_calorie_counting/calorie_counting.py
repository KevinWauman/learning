f = open("input.txt", "r")

input = f.read()

grouped_per_dwarf = input.split("\n\n")

max = -1

for g in grouped_per_dwarf:
    temp_sum = 0
    for _ in g.split("\n"):
        temp_sum += int(_)
    if temp_sum > max:
        max = temp_sum

print(max)