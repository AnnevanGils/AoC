import numpy as np

fname = "2023/day13/input.txt"


result1 = 0

with open(fname, "r") as f:
    patterns = f.read().split("\n\n")
    for pattern in patterns:
        lines = pattern.split("\n")
        a = np.array([[l for l in line] for line in lines])

        # mirror between rows
        for i in range(a.shape[0] - 1):
            i1 = i
            i2 = i + 1
            mirror = True
            while (i1 >= 0) and (i2 < a.shape[0]):
                if "".join(a[i1].tolist()) != "".join(a[i2].tolist()):
                    mirror = False
                    break
                i1 -= 1
                i2 += 1

            if mirror:
                result1 += 100 * (i + 1)
                break

        # mirror between columns
        for j in range(a.shape[1] - 1):
            j1 = j
            j2 = j + 1
            mirror = True
            while (j1 >= 0) and (j2 < a.shape[1]):
                if "".join(a[:, j1].tolist()) != "".join(a[:, j2].tolist()):
                    mirror = False
                    break
                j1 -= 1
                j2 += 1

            if mirror:
                result1 += j + 1
                break

print("result 1:", result1)

# part 2

result2 = 0

with open(fname, "r") as f:
    patterns = f.read().split("\n\n")
    for pattern in patterns:
        print("new pattern")
        lines = pattern.split("\n")
        a = np.array([[l for l in line] for line in lines])

        # mirror between rows
        for i in range(a.shape[0] - 1):
            i1 = i
            i2 = i + 1
            mirror = True
            smudge_repaired = False
            while (i1 >= 0) and (i2 < a.shape[0]):
                truth_array = a[i1] != a[i2]
                if (np.sum(truth_array) == 1) and not smudge_repaired:
                    smudge_repaired = True

                elif "".join(a[i1].tolist()) != "".join(a[i2].tolist()):
                    mirror = False
                    break
                i1 -= 1
                i2 += 1

            if mirror and smudge_repaired:
                print("mirror after row ", i)
                result2 += 100 * (i + 1)
                row_mirror = True
                break

        # mirror between columns
        for j in range(a.shape[1] - 1):
            j1 = j
            j2 = j + 1
            mirror = True
            smudge_repaired = False
            while (j1 >= 0) and (j2 < a.shape[1]):
                truth_array = a[:, j1] != a[:, j2]
                if (np.sum(truth_array) == 1) and not smudge_repaired:
                    print(f"smudge repaired between cols {j1} and {j2}")
                    smudge_repaired = True

                elif "".join(a[:, j1].tolist()) != "".join(a[:, j2].tolist()):
                    mirror = False
                    break
                j1 -= 1
                j2 += 1

            if mirror and smudge_repaired:
                print("mirror after column ", j)
                result2 += j + 1
                break

        print()

print("result 2:", result2)
