import math
import re

def parse_stacks(lines, num_stacks):
    indexes_line = get_indexes_line(lines)
    stack_lines = lines[:indexes_line]
    
    stack_indexes = [i for i, stack in enumerate(lines[indexes_line]) if stack.strip()]
    stacks = {i + 1: [] for i in range(num_stacks)}

    for line in stack_lines:
        for i, pos in enumerate(stack_indexes):
            if line[pos].strip():
                  stacks[i + 1].append(line[pos])
    return stacks

def get_indexes_line(lines):
    return next(filter(lambda x: x[1][1] == '1', enumerate(lines)), (-1, ''))[0]
    
def get_num_stacks(lines):
    return int(math.ceil(len(lines[0]) / 4))

def parse_instructions(lines, num_stacks):
    return map(lambda si: [int(i) for i in re.findall(r'(\d+)', si)], lines[num_stacks + 1:])

def organize(stacks, instructions):
    for instruction in instructions:
        stack = stacks[instruction[1]][:instruction[0]]
        del stacks[instruction[1]][:instruction[0]]
        # stack.reverse()
        stacks[instruction[2]] = stack + stacks[instruction[2]]

def get_top(stacks):
    return ''.join([stack[:1][0] for stack in stacks.values()])

def rearrange():
    file = open('input', 'r')
    lines = file.readlines()

    num_stacks = get_num_stacks(lines)
    stacks = parse_stacks(lines, num_stacks)
    instructions = parse_instructions(lines, num_stacks)
    organize(stacks, instructions)

    print(f'** Top stacks: {get_top(stacks)}')

if __name__ == "__main__":
    rearrange()
