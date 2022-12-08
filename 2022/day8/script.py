import numpy as np

with open("day8/input.txt", 'r') as f:
    lines = f.readlines()
    gridsize = len(lines[0].strip('\n'))
    grid = np.zeros(shape=(gridsize, gridsize))

    for i, line in enumerate(lines):
        for j, l in enumerate(line.strip('\n')):
            grid[i,j] = int(l)

def check_shorter(t, tree_line):
    # returns true if every tree in tree line is shorter than t
    for tree in tree_line:
        if(tree >= t):
            return False
    return True

count = 0
for i, row in enumerate(grid):
    for j, column in enumerate(row):
        # print(grid[:i, j])
        # print(grid[i, :j])
        # print(grid[i+1:, j])
        # print(grid[i, j+1:])
        b1 = check_shorter(grid[i, j], grid[:i, j])
        b2 = check_shorter(grid[i, j], grid[i, :j])
        b3 = check_shorter(grid[i, j], grid[i+1:, j])
        b4 = check_shorter(grid[i, j], grid[i, j+1:])
        if(b1 | b2 | b3 | b4):
            count += 1     

print(count)

# part 2
def trees_in_line_of_sight(t, tree_line):
    cnt = 0
    for tree in tree_line:
        if(t <= tree):
            return cnt + 1
        cnt += 1
    return cnt

max_scenic_score = 0

for i, row in enumerate(grid):
    for j, column in enumerate(row):        
        # print(grid[i, j])
        # print(grid[:i, j][::-1])
        # print(grid[i, :j][::-1])
        # print(grid[i+1:, j])
        # print(grid[i, j+1:])
        s1 = trees_in_line_of_sight(grid[i, j], grid[:i, j][::-1])
        s2 = trees_in_line_of_sight(grid[i, j], grid[i, :j][::-1])
        s3 = trees_in_line_of_sight(grid[i, j], grid[i+1:, j])
        s4 = trees_in_line_of_sight(grid[i, j], grid[i, j+1:])

        max_scenic_score = max(s1*s2*s3*s4, max_scenic_score)
          
print(max_scenic_score)