import numpy as np
import time

fname = "2023/day11/input.txt"

with open(fname, "r") as f:
    lines = f.read().split("\n")
    cols = len(lines[0])
    rows = len(lines)
    a = np.full(shape=(rows, cols), fill_value=np.nan, dtype=int)

    for i, line in enumerate(lines):
        a[i] = np.array([1 if c == "#" else 0 for c in line])


print(a)
print()

empty_rows = np.argwhere(np.sum(a, 1) == 0).flatten()
empty_cols = np.argwhere(np.sum(a, 0) == 0).flatten()


def get_pos_key(coords):
    return f"{coords[0]}_{coords[1]}"


def get_star_pair_key(coord1, coord2):
    coords = sorted([coord1, coord2])
    return f"{coords[0][0]}_{coords[0][1]}__{coords[1][0]}_{coords[1][1]}"


star_coords = np.argwhere(a == 1)
stars = [get_pos_key(c) for c in star_coords]
print("stars", stars)


def get_next_to_visit(current_coords, visited):
    l = []
    for i, j in current_coords:
        current_path_length = visited[get_pos_key([i, j])]
        for pi, pj in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
            if (pi >= 0) and (pi < rows) and (pj >= 0) and (pj < cols):
                pos_key = get_pos_key([pi, pj])
                if pos_key not in visited:
                    if (i != pi) and (pi in empty_rows):
                        # check if row that's being moved into is empty row
                        # step counts double
                        stepsize = 2
                    elif (j != pj) and (pj in empty_cols):
                        stepsize = 2
                    else:
                        stepsize = 1
                    visited[pos_key] = current_path_length + stepsize
                    l.append([pi, pj])
    return l


star_pairs = {}

time1 = time.time()

for n, coords in enumerate(star_coords):
    print(f"{n} / {len(star_coords)}, {time.time() - time1}s")
    coords = coords.tolist()
    # find nearest star
    visited = {}
    visited[get_pos_key(coords)] = 0
    current_coords = [coords]
    while True:
        # step into neighbors
        current_coords = get_next_to_visit(current_coords, visited)

        # check if star is reached (multiple can be reached at the same time)
        for cc in current_coords:
            cc_key = get_pos_key(cc)
            if cc_key in stars:
                star_pairs[get_star_pair_key(cc, coords)] = visited[cc_key]

        if len(current_coords) == 0:
            break

# print(star_pairs)
print("number of pairs:", len(star_pairs.keys()))
result1 = sum([d for d in star_pairs.values()])

print()
print("result1: ", result1)
