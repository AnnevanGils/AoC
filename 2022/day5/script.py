import numpy as np
import re

# choose part = 1 or part = 2
part = 2

with open("day5/input.txt", 'r') as f:
    config_lines = []
    operations = []
    start_opp = False
    pattern = 'move (\d+) from (\d) to (\d)'
    for line in f.readlines():
        if(line == "\n"):
            start_opp = True
            continue
        if not start_opp:
            # add crate config lines to list
            config_lines.append(line)
        else:
            # parse operation lines
            g = re.search(pattern, line).groups()
            operations.append((int(g[0]), int(g[1]), int(g[2])))

# define stacks of crates
stacks = {int(n): [] for n in config_lines[-1].strip('\n').split('   ')}

# parse initial configuration of crates
for line in config_lines[:-1][::-1]:
    for i, elem in enumerate(line.strip('\n')):
        if(i%4 == 1):
            crate_nr = int(np.floor(i / 4) + 1)
            if(elem != ' '):
                stacks[crate_nr].append(elem)

# execute operations
for op in operations:
    nr_moved = op[0]
    from_stack = op[1]
    to_stack = op[2]

    crates_moved = stacks[from_stack][-nr_moved:]
    if(part == 1):
        stacks[to_stack].extend(crates_moved[::-1])
    elif(part == 2):
        stacks[to_stack].extend(crates_moved)
    stacks[from_stack] = stacks[from_stack][:-nr_moved]


top_crates = ''
for stack, crates in stacks.items():
    top_crates += crates[-1]

print(top_crates)
            