tail_visited = []
import numpy as np

def catch_up_tail_compact(pos_head_new, pos_tail_old):
    v_tail = pos_tail_old[0]
    h_tail = pos_tail_old[1]
    # check if on same axis
    same_axis = (pos_head_new[0] == pos_tail_old[0] or pos_head_new[1] == pos_tail_old[1])

    sign_v = np.sign(pos_head_new[0] - pos_tail_old[0])
    sign_h = np.sign(pos_head_new[1] - pos_tail_old[1])
    diff_v = abs(pos_head_new[0] - pos_tail_old[0])
    diff_h = abs(pos_head_new[1] - pos_tail_old[1])

    # update per axis
    # vertical axis
    if(diff_v > 1):
        v_tail += sign_v * diff_v -1 * sign_v
        if not same_axis:
            # determine direction for stepping h_tail to
            # if head left from tail, move h_tail to left
            # if head right from tail, move h_tail to right
            h_tail += sign_h

    # horizontal axis
    elif(diff_h > 1):
        h_tail += sign_h * diff_h -1 * sign_h
        if not same_axis:
            v_tail += sign_v
    
    return [v_tail, h_tail]

# part 1
with open("day9/input.txt", 'r') as f:
    pos_head = [0,0]
    pos_tail = [0,0]
    tail_visited.append(pos_tail)
    for line in f.readlines():
        direction, steps = line.strip("\n").split(" ")
        steps = int(steps)
        
        for i in range(steps):
            if(direction == 'R'):
                pos_head[1] += 1
            elif(direction == 'U'):
                pos_head[0] += 1
            elif(direction == 'D'):
                pos_head[0] -= 1
            elif(direction == 'L'):
                pos_head[1] -= 1

            pos_tail = catch_up_tail_compact(pos_head, pos_tail)
            tail_visited.append(pos_tail)

tail_visited_str = ["_".join([str(s) for s in a]) for a in tail_visited]
print(len(set(tail_visited_str)))

# part 2
tail_visited_2 = []
with open("day9/input.txt", 'r') as f:
    pos_nodes = [[0,0] for i in range(10)]
    tail_visited_2.append(pos_nodes[-1])
    for line in f.readlines():
        direction, steps = line.strip("\n").split(" ")
        steps = int(steps)
        
        for i in range(steps):
            if(direction == 'R'):
                pos_nodes[0][1] += 1
            elif(direction == 'U'):
                pos_nodes[0][0] += 1
            elif(direction == 'D'):
                pos_nodes[0][0] -= 1
            elif(direction == 'L'):
                pos_nodes[0][1] -= 1
            
            for n, node in enumerate(pos_nodes[1:]):
                pos_nodes[n+1] = catch_up_tail_compact(pos_nodes[n], node)

            tail_visited_2.append(pos_nodes[-1])

tail_visited_2_str = ["_".join([str(s) for s in a]) for a in tail_visited_2]
print(len(set(tail_visited_2_str)))