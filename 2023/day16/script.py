import numpy as np

fname = "2023/day16/input.txt"

with open(fname, "r") as f:
    lines = f.read().split("\n")
    a = np.full((len(lines), len(lines[0])), fill_value="n")
    for i, line in enumerate(lines):
        a[i] = np.array([s for s in line])


dir_to_operator = {
    "up": np.array([-1, 0]),
    "right": np.array([0, 1]),
    "down": np.array([1, 0]),
    "left": np.array([0, -1]),
}

left_mirror = {"right": "down", "left": "up", "down": "right", "up": "left"}
right_mirror = {"right": "up", "left": "down", "up": "right", "down": "left"}


def get_history_hash(head, direction):
    return f"{head[0]}_{head[1]}_{direction}"


def find_number_of_visited_tiles(head, direction):
    visited = np.full(a.shape, fill_value=False)

    # current positions of laser beam heads
    heads = [head]
    # current beam directions
    directions = [direction]

    states_history = []

    while len(heads) > 0:
        # throw out heads that lead to infinite cycles`
        i = 0
        while i < len(heads):
            if get_history_hash(heads[i], directions[i]) in states_history:
                heads.pop(i)
                directions.pop(i)
            else:
                i += 1

        # handle optics
        for i, head in enumerate(heads):
            # add state to state history and mark as visited
            states_history.append(get_history_hash(head, directions[i]))
            visited[*head] = True

            if (a[*head] == "|") and (directions[i] in ["right", "left"]):
                # change current direction
                directions[i] = "down"
                # spawn new head + direction
                heads.append(np.copy(head))
                directions.append("up")
            elif (a[*head] == "-") and (directions[i] in ["up", "down"]):
                # change current direction
                directions[i] = "right"
                # spawn new head + direction
                heads.append(np.copy(head))
                directions.append("left")
            elif a[*head] == "\\":
                directions[i] = left_mirror[directions[i]]
            elif a[*head] == "/":
                directions[i] = right_mirror[directions[i]]

        # progress beams
        i = 0
        while i < len(heads):
            heads[i] += dir_to_operator[directions[i]]
            head = heads[i]
            if (
                (np.sum(head < 0) > 0)
                or (head[0] > a.shape[0] - 1)
                or (head[1] > a.shape[1] - 1)
            ):
                # print("removing", head)
                heads.pop(i)
                directions.pop(i)
                # print("heads after removal", heads)
                # print("directions", directions)
                # print()
            else:
                i += 1

    return np.sum(visited)


result1 = find_number_of_visited_tiles(np.array([0, 0]), "right")

print("part 1:", result1)
print()

# part 2

max_visited = 0

# top and bottom rows
for j in range(a.shape[1]):
    max_visited = max(
        max_visited, find_number_of_visited_tiles(np.array([0, j]), "down")
    )
    max_visited = max(
        max_visited, find_number_of_visited_tiles(np.array([a.shape[0] - 1, j]), "up")
    )
    print(f"columns {j+1}/{a.shape[1]}")

print()

for i in range(a.shape[0]):
    max_visited = max(
        max_visited, find_number_of_visited_tiles(np.array([i, 0]), "right")
    )
    max_visited = max(
        max_visited, find_number_of_visited_tiles(np.array([i, a.shape[1] - 1]), "left")
    )
    print(f"columns {i+1}/{a.shape[0]}")

print()
print("part 2:", max_visited)
