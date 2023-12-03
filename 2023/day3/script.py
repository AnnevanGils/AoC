from collections import defaultdict

fname = "2023/day3/input.txt"

numbers = []
result1 = 0

with open(fname, "r") as f:
    lines = f.readlines()

    i_max = len(lines[0].strip("\n")) - 1
    j_max = len(lines) - 1

    for i, line in enumerate(lines):
        # end of line char acts as padding, same as .
        new_number = ""
        for j, c in enumerate(line):
            if c.isdigit():
                new_number += c
            else:
                if new_number != "":
                    # store number, find neighboring symbols
                    number_dict = {"number": int(new_number), "adjacent_to": []}
                    # look at all neighbors
                    i_start = max(0, i - 1)
                    i_end = min(i + 1, i_max)
                    j_start = max(0, j - len(new_number) - 1)
                    j_end = min(j, j_max)
                    for i_s in range(i_start, i_end + 1):
                        for k, s in enumerate(lines[i_s][j_start : j_end + 1]):
                            if not (s.isdigit() or s == "." or s == "\n"):
                                symbol_dict = {"symbol": s, "loc": (i_s, j_start + k)}
                                number_dict["adjacent_to"].append(symbol_dict)

                    # add to result
                    if len(number_dict["adjacent_to"]) > 0:
                        result1 += number_dict["number"]

                    # add to numbers list
                    numbers.append(number_dict)

                    # reset number
                    new_number = ""

# for number_dict in numbers:
#     print(number_dict)
# print()

print("part 1: ", result1)

# part 2

result2 = 0
gears = defaultdict(list)

for number_dict in numbers:
    n = number_dict["number"]
    for symbol_dict in number_dict["adjacent_to"]:
        if symbol_dict["symbol"] == "*":
            loc = symbol_dict["loc"]
            gear_id = f"{loc[0]}_{loc[1]}"
            gears[gear_id].append(n)

# print(gears)

for n_list in gears.values():
    if len(n_list) == 2:
        result2 += n_list[0] * n_list[1]

print()
print("part 2: ", result2)
