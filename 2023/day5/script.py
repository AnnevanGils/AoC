import numpy as np

fname = "2023/day5/input.txt"

# source column
j_s = 1
# destination column
j_d = 0
# range length column
j_r = 2


def apply_map(seeds, range_data, map_name=None):
    seed_mapping = np.full(len(seeds), fill_value=np.nan, dtype=int)

    for i, s in enumerate(seeds):
        s_outside_any_range = (s < range_data[0, j_s]) + (
            s >= (range_data[-1, j_s] + range_data[-1, j_r])
        )
        if s_outside_any_range:
            seed_mapping[i] = s
        else:
            # first occurrence in range_data where s falls in source range
            range_idx = np.argmax(
                (s >= range_data[:, j_s])
                * (s < range_data[:, j_s] + range_data[:, j_r])
            )

            # apply mapping
            depth = s - range_data[range_idx, j_s]
            seed_mapping[i] = range_data[range_idx, j_d] + depth

    if not map_name == None:
        print(f"applying {map_name}")
        print(seed_mapping)
        print()

    return seed_mapping


def sort_range_data(range_data, j_sort):
    return range_data[np.argsort(range_data[:, j_sort])]


maps = {}

with open(fname, "r") as f:
    for block in f.read().split("\n\n"):
        if "seeds: " in block:
            seeds = np.array([int(d) for d in block.split(": ")[1].split(" ")])
            seeds_init = np.copy(seeds)
        else:
            lines = block.split("\n")
            map_name = lines[0].replace(" map:", "")
            range_data = np.fromstring(
                "\n".join(lines[1:]), sep=" ", dtype=int
            ).reshape(len(lines[1:]), -1)
            # sort range data on source
            range_data = sort_range_data(range_data, j_s)

            # store in maps for part 2
            maps[map_name] = range_data

            seeds = apply_map(seeds, range_data, map_name if "test2" in fname else None)

print("part 1: ", np.min(seeds))
print()


# part 2

seed_ranges = seeds_init.reshape(-1, 2)

for map_name, range_data in maps.items():
    new_seed_ranges = []
    for start, length in seed_ranges:
        while length > 0:
            # seed range entirely lower or entirely higher than any mapping source range
            s_range_no_overlap = ((start + length - 1) < range_data[0, j_s]) + (
                start >= (range_data[-1, j_s] + range_data[-1, j_r])
            )

            if s_range_no_overlap:
                new_seed_ranges.append([start, length])
                break
            else:
                # first occurrence in range_data where s_range falls in source range
                range_idx = np.argmax(
                    ((start + length - 1) >= range_data[:, j_s])
                    * (start < range_data[:, j_s] + range_data[:, j_r])
                )

                # apply range from the left, apply overlap, ignore part to the right
                length_left = max(range_data[range_idx, j_s] - start, 0)
                if length_left != 0:
                    new_seed_ranges.append([start, length_left])

                length_remaining_in_range = max(
                    min(
                        range_data[range_idx, j_s] + range_data[range_idx, j_r] - start,
                        range_data[range_idx, j_r],
                    ),
                    0,
                )
                length_overlap = min(length_remaining_in_range, length - length_left)
                if length_overlap != 0:
                    offset = range_data[range_idx, j_r] - length_remaining_in_range
                    new_seed_ranges.append(
                        [range_data[range_idx, j_d] + offset, length_overlap]
                    )

                # adjust start and length
                length = length - length_left - length_overlap
                start = range_data[range_idx, j_s] + range_data[range_idx, j_r]

    seed_ranges = new_seed_ranges

print("part 2: ", np.min(np.array(seed_ranges)[:, 0]))
