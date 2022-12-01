a = {}

with open("input.txt", 'r') as f:
    current_elf = 0
    for line in f.readlines():
        if(line == "\n"):
            current_elf += 1
        else:
            if(current_elf not in a):
                a[current_elf] = []
            a[current_elf].append(int(line))

# part 1
max_cal = 0
for k, v in a.items():
    max_cal = max(max_cal, sum(v))

print(max_cal)
print()

# part 2
top_3 = [0, 0, 0]
for k, v in a.items():
    top_3.sort()
    for i, m in enumerate(top_3):
        if(sum(v) > m):
            top_3[i] = sum(v)
            break

print(sum(top_3))

