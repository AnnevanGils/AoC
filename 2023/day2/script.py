from collections import defaultdict

games = defaultdict(list)

with open("2023/day2/input.txt", "r") as f:
    for line in f.readlines():
        splits = line.split(":")
        game = int(splits[0].replace("Game", ""))
        rest = splits[1].strip()
        tuples = rest.split("; ")
        for t in tuples:
            values = t.split(", ")
            r = None
            g = None
            b = None
            for v in values:
                if "red" in v:
                    r = int(v.replace("red", ""))
                if "green" in v:
                    g = int(v.replace("green", ""))
                if "blue" in v:
                    b = int(v.replace("blue", ""))
            r = r if r != None else 0
            g = g if g != None else 0
            b = b if b != None else 0
            games[game].append((r, g, b))

# print(games)
# print()

r_max = 12
g_max = 13
b_max = 14

# part 1

result = 0
for g, l in games.items():
    valid = True
    for t in l:
        if (t[0] > r_max) or (t[1] > g_max) or (t[2] > b_max):
            valid = False
            break
    if valid:
        result += g

print("part 1: ", result)
print()

# part 2
result2 = 0
for g, l in games.items():
    # the minimum values to play the game are the maximum from all the sets
    r_min, g_min, b_min = 0, 0, 0
    for t in l:
        r_min = max(t[0], r_min)
        g_min = max(t[1], g_min)
        b_min = max(t[2], b_min)

    result2 += r_min * g_min * b_min

print("part 2: ", result2)
