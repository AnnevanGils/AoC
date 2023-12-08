from collections import defaultdict
import re
import math

fname = "2023/day8/input.txt"


class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.left = None
        self.right = None


node_list = {}
start_nodes_p2 = []

with open(fname, "r") as f:
    instruction, nodes = f.read().split("\n\n")

    nodes = nodes.split("\n")

    for node in nodes:
        p, cl, cr = re.match("(.*) = \((.*), (.*)\)", node).groups()

        left_child = Node(cl) if not cl in node_list else node_list[cl]
        node_list[cl] = left_child

        right_child = Node(cr) if not cr in node_list else node_list[cr]
        node_list[cr] = right_child

        parent = Node(p) if not p in node_list else node_list[p]
        parent.left = left_child
        parent.right = right_child
        node_list[p] = parent

        if p[-1] == "A":
            start_nodes_p2.append(p)


def gen_instruction(instruction):
    i = 0
    while True:
        if i > len(instruction) - 1:
            i = 0
        yield instruction[i]
        i += 1


if "AAA" in node_list:
    gen = gen_instruction(instruction)

    steps = 0
    current_node = node_list["AAA"]

    while current_node.name != "ZZZ":
        current_node = current_node.left if next(gen) == "L" else current_node.right
        steps += 1

    print("part 1:", steps)

# part 2

gen = gen_instruction(instruction)


current_nodes = [node_list[n] for n in start_nodes_p2]
node_idx = [i for i in range(len(current_nodes))]
min_steps = [0 for _ in node_idx]

steps = 0

while len(current_nodes) > 0:
    instr = next(gen)
    new_current_nodes = [n.left if instr == "L" else n.right for n in current_nodes]
    steps += 1
    for i, n in enumerate(new_current_nodes):
        if n.name[-1] == "Z":
            min_steps[node_idx[i]] = steps
            new_current_nodes.pop(i)
            node_idx.pop(i)

    current_nodes = new_current_nodes


print("part 2:", math.lcm(*min_steps))
