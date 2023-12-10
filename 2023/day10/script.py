import numpy as np
import sys

sys.setrecursionlimit(100000)

fname = "2023/day10/input.txt"
show_path = False

symbol_to_int = {s: ord(s) for s in "S7-F.J|L"}
print(symbol_to_int)

with open(fname, "r") as f:
    lines = f.read().split("\n")
    len_line = len(lines[0])
    padding = (len_line + 2) * "B"
    data = padding + "B" + "BB".join(lines) + "B" + padding
    a = np.fromstring(data, dtype=np.ubyte)
    a = np.reshape(a, (-1, len_line + 2))


for row in a:
    print("".join([chr(n) for n in row]))
print()

# expanded a for part 2
a_expanded = np.full(
    shape=(3 * (a.shape[0] - 2), 3 * (a.shape[1]) - 2), fill_value=ord(".")
)

# list of filters
int_to_filter = {
    ord("L"): ".|..L-...",
    ord("F"): "....F-.|.",
    ord("J"): ".|.-J....",
    ord("7"): "...-7..|.",
    ord("|"): ".|..|..|.",
    ord("-"): "...---...",
}
int_to_filter = {
    k: np.fromstring(v, dtype=np.ubyte).reshape(3, 3) for k, v in int_to_filter.items()
}

# find start coords
i, j = np.argwhere(a == ord("S"))[0]
current_pipe = None
count = 0
north = [ord(s) for s in "|F7"]
west = [ord(s) for s in "-LF"]
south = [ord(s) for s in "|JL"]
east = [ord(s) for s in "-7J"]
s_real_translate = {
    "1100": "L",
    "1010": "|",
    "1001": "J",
    "0110": "F",
    "0101": "-",
    "0011": "7",
}
s_real_key = "".join(
    [
        "1" if b else "0"
        for b in [
            a[i - 1, j] in north,
            a[i, j + 1] in east,
            a[i + 1, j] in south,
            a[i, j - 1] in west,
        ]
    ]
)
a[i, j] = ord(s_real_translate[s_real_key])
# walk loop until at start again
while True:
    # adjust expanded a for part 2
    if (i > 0) and (i < a.shape[0]) and (j > 0) and (j < a.shape[1]):
        a_expanded[
            (i - 1) * 3 : (i - 1) * 3 + 3, (j - 1) * 3 : (j - 1) * 3 + 3
        ] = int_to_filter[a[i, j]]

    a[i, j] = ord("P")
    if (a[i - 1, j] in north) and not (current_pipe in [ord(s) for s in "7F-"]):
        i, j = i - 1, j
    elif (a[i, j + 1] in east) and not (current_pipe in [ord(s) for s in "7J|"]):
        i, j = i, j + 1
    elif (a[i + 1, j] in south) and not (current_pipe in [ord(s) for s in "LJ-"]):
        i, j = i + 1, j
    elif (a[i, j - 1] in west) and not (current_pipe in [ord(s) for s in "LF|"]):
        i, j = i, j - 1
    else:
        print("dead end")
        print("max count", count)
        result1 = int(np.ceil(count / 2))
        print("max path distance", result1)
        print()
        print("result 1:", result1)
        print()
        break

    current_pipe = a[i, j]
    count += 1

if show_path:
    for row in a:
        print("".join([chr(n) for n in row]))
    print()

if "test" in fname:
    for row in a_expanded:
        print("".join([chr(n) for n in row]))
    print()

# part 2
# change outer layer of a_expanded into padding B
a_expanded[0, :] = np.full(a_expanded.shape[1], fill_value=ord("B"))
a_expanded[:, 0] = np.full(a_expanded.shape[0], fill_value=ord("B"))
a_expanded[a_expanded.shape[0] - 1, :] = np.full(
    a_expanded.shape[1], fill_value=ord("B")
)
a_expanded[:, a_expanded.shape[1] - 1] = np.full(
    a_expanded.shape[0], fill_value=ord("B")
)

if "test" in fname:
    for row in a_expanded:
        print("".join([chr(n) for n in row]))
    print()

# keep track of visited for performance purposes?
visited = np.full(shape=a_expanded.shape, fill_value=False)


def fill_outer(i, j):
    visited[i, j] = True
    if a_expanded[i, j] == ord("B"):
        pass
    elif a_expanded[i, j] == ord("."):
        a_expanded[i, j] = ord("B")
        if not visited[i - 1, j]:
            fill_outer(i - 1, j)
        if not visited[i, j - 1]:
            fill_outer(i, j - 1)
        if not visited[i, j + 1]:
            fill_outer(i, j + 1)
        if not visited[i + 1, j]:
            fill_outer(i + 1, j)
    else:
        # encountered path
        pass


# fill places outside path with padding  B
for i in range(1, a_expanded.shape[0] - 1):
    fill_outer(i, 1)
    fill_outer(i, a_expanded.shape[1] - 2)
for j in range(1, a_expanded.shape[1] - 1):
    fill_outer(1, j)
    fill_outer(a_expanded.shape[0] - 2, j)

if "test" in fname:
    for row in a_expanded:
        print("".join([chr(n) for n in row]))
    print()

result2 = 0

# stride a_expanded
for i in range(1, a.shape[0] - 1):
    for j in range(1, a.shape[1] - 1):
        window_str = "".join(
            chr(n)
            for n in a_expanded[
                (i - 1) * 3 : (i - 1) * 3 + 3, (j - 1) * 3 : (j - 1) * 3 + 3
            ].flatten()
        )
        if window_str == "." * 9:
            result2 += 1

print("result 2:", result2)
