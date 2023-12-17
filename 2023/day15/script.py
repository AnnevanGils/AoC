from collections import defaultdict

fname = "2023/day15/input.txt"


def hash_key(key):
    result = 0
    for s in key:
        result += ord(s)
        result *= 17
        result %= 256
    return result


result1 = 0

labels = [[] for _ in range(256)]
focal_lenghts = [[] for _ in range(256)]

with open(fname, "r") as f:
    steps = f.read().split(",")
    for step in steps:
        # part 1
        result1 += hash_key(step)

        # part 2
        if "-" in step:
            label, _ = step.split("-")
            key = hash_key(label)
            lens_list = labels[key]
            if label in lens_list:
                i = lens_list.index(label)
                labels[key] = lens_list[:i] + lens_list[i + 1 :]
                focal_list = focal_lenghts[key]
                focal_lenghts[key] = focal_list[:i] + focal_list[i + 1 :]
        elif "=" in step:
            label, f = step.split("=")
            key = hash_key(label)
            lens_list = labels[key]
            if label in lens_list:
                i = lens_list.index(label)
                focal_lenghts[key][i] = int(f)
            else:
                lens_list.append(label)
                focal_lenghts[key].append(int(f))


print("part 1:", result1)
print()

result2 = 0

for i, label_list in enumerate(labels):
    for j, f in enumerate(focal_lenghts[i]):
        result2 += (i + 1) * (j + 1) * f

print("part 2:", result2)
