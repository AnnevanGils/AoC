import numpy as np
import time

def print_matrix(matrix, pad=0, end=' '):
    nr_integers_top = len(str(matrix.shape[1] + pad))
    nr_integers_side = len(str(matrix.shape[0]))
    for nr in range(nr_integers_top):
        print(" " + " "*nr_integers_side + " ".join([str(k + pad)[nr] if len(str(k + pad)) >= nr else " " for k in range(matrix.shape[1])]))
    for i, row in enumerate(matrix):        
        if(i != 0):
            print()
        print(str(i) + " " * ( nr_integers_side - len(str(i)) ), end=' ')
        for j, c in enumerate(row):
            print(c, end=end)
    print()

def update_matrix(matrix, pad=0, end=" "):
    time.sleep(0.1)
    print("\r" + "".join(["\033[A" for i in range(matrix.shape[0]+1)]))
    for i, row in enumerate(matrix):
        if(i != 0):
            print()
            print(i, end=' ')
        else:
            print(i, end=' ')
        for j, c in enumerate(row):
            print(c, end=end)
    print()

wall = np.full(shape=(200, 700), fill_value='.')

max_depth = 0
leftmost = wall.shape[1]
rightmost = 0

with open("day14/input.txt", 'r') as f:
    for line in f.readlines():
        segments = line.strip("\n").split(" -> ")
        print()
        for s, segment in enumerate(segments[:-1]):
            start_pos = [int(i) for i in segment.split(",")]
            end_pos = [int(i) for i in segments[s+1].split(",")]
            # slice wall
            start_pos_0 = np.min([start_pos[1], end_pos[1]])
            end_pos_0 = np.max([start_pos[1], end_pos[1]])
            start_pos_1 = np.min([start_pos[0], end_pos[0]])
            end_pos_1 = np.max([start_pos[0], end_pos[0]])
            wall[start_pos_0:end_pos_0+1,start_pos_1:end_pos_1+1] = '#'

            max_depth = np.max([max_depth, start_pos_0, end_pos_0])
            leftmost = np.min([leftmost, start_pos_1, end_pos_1])
            rightmost = np.max([rightmost, start_pos_1, end_pos_1])

# np.set_printoptions(threshold=1000000, linewidth=100000, formatter={'str_kind': lambda x: x})

sand_start_pos = [0, 500]
wall[sand_start_pos[0], sand_start_pos[1]] = '+'

wall_p2 = np.copy(wall)

print("max_depth: ", max_depth)
# print_matrix(wall[:max_depth+1, leftmost-2:rightmost+3], pad=leftmost-2)


def move_sand(origin, grid, max_depth):
    # try positions one down, one down left, one down right
    try_positions = [[origin[0]+1, origin[1]], [origin[0]+1, origin[1]-1], [origin[0]+1, origin[1]+1]]
    new_pos = None
    
    for pos in try_positions:
        if(grid[pos[0], pos[1]] == '.'):
            new_pos = pos
            break
    
    new_depth = origin[0]-1
    
    # stopping condition: sand can't be moved further 
    if(new_pos == None):
        # print(f"returning origin: {origin}")
        return origin
    # stopping condition: sand has passed max depth (it's sinking into the void)
    elif(new_depth > max_depth):
        # print(new_depth)  
        return None
    # proceed to move sand
    else:
        # print(f"moving sand to {new_pos}")
        return move_sand(new_pos, grid, max_depth)
        

def drop_sand(sand_start_pos, grid, max_depth):
    sand_count = 0
    while True:
        new_pos = move_sand(sand_start_pos, grid, max_depth)
        # print(f"received new pos: {new_pos}")
        if(new_pos == None):
            print(f"Reached max sand capacity of {sand_count}")
            return sand_count
        else:
            # print(f"new pos: {new_pos}")
            grid[new_pos[0], new_pos[1]] = 'o'
            sand_count += 1
            # update_matrix(grid[:150, 400:510])



count = drop_sand(sand_start_pos, wall, max_depth)

print_matrix(wall[:max_depth+1, leftmost-2:rightmost+3], pad=leftmost-2)

print()
print(f"Max sand capacity: {count}")

# part 2
wall_p2[max_depth+2, :] = '#'
max_depth_p2 = max_depth + 2

# print_matrix(wall_p2[:max_depth_p2+1, leftmost-2:rightmost+3], pad=leftmost-2)

def move_sand_p2(origin, grid):
    # try positions one down, one down left, one down right
    try_positions = [[origin[0]+1, origin[1]], [origin[0]+1, origin[1]-1], [origin[0]+1, origin[1]+1]]
    new_pos = None
    
    for pos in try_positions:
        if(grid[pos[0], pos[1]] == '.'):
            new_pos = pos
            break
    
    new_depth = origin[0]-1
    
    # stopping condition: sand can't be moved further 
    if(new_pos == None):
        # print(f"returning origin: {origin}")
        return origin
    # proceed to move sand
    else:
        # print(f"moving sand to {new_pos}")
        return move_sand(new_pos, grid, max_depth)

def drop_sand_p2(sand_start_pos, grid):
    sand_count = 0
    while True:
        new_pos = move_sand_p2(sand_start_pos, grid)
        # print(f"received new pos: {new_pos}")
        if(new_pos[0] == sand_start_pos[0] and new_pos[1] == sand_start_pos[1]):
            grid[new_pos[0], new_pos[1]] = 'o'
            print(f"Reached max sand capacity of {sand_count + 1}")
            return sand_count + 1
        else:
            # print(f"new pos: {new_pos}")
            grid[new_pos[0], new_pos[1]] = 'o'
            sand_count += 1
            # update_matrix(grid[:150, 400:510])

count2 = drop_sand_p2(sand_start_pos, wall_p2)

print_matrix(wall_p2[:max_depth_p2+1, leftmost-2:rightmost+3], pad=leftmost-2)

print()
print(f"Max sand capacity: {count2}")