import numpy as np

fname = "2023/day9/input.txt"

result1 = 0
result2 = 0

with open(fname, "r") as f:
    lines = f.read().split("\n")

    for line in lines:
        a = np.fromstring(line, sep=" ", dtype=int)

        deltas = [a[-1]]
        deltas_reverse = [a[0]]
        while np.sum(np.abs(a)) != 0:
            a = a[1:] - a[:-1]
            deltas.append(a[-1])
            deltas_reverse.append(a[0])

        result1 += sum(deltas)

        new_left = 0
        for n in deltas_reverse[-1::-1]:
            new_left = n - new_left

        result2 += new_left

print("part 1:", result1)
print()
print("part 2:", result2)
