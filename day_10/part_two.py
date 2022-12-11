def get_cycles(lines):
    x = 1
    next_cycle = 0
    cycles = {}

    for line in lines:
        i = line.strip().split()
        c, value = (2, int(i[1])) if i[0] == 'addx' else (1, 0)

        for i in range(next_cycle, next_cycle + c):
            if i not in cycles:
                cycles[i] =  cycles[i - 1] if i > 2 else 1

        next_cycle = next_cycle + c
        x = x + value
        cycles[next_cycle] = x
    return next_cycle, cycles

def print_lines(total_cycles, cycles):
    LINE_LENGTH = 40
    x = 1
    current_cycle = 1
    sprite = [x - 1, x, x + 1]

    for _ in range(0, int(total_cycles / LINE_LENGTH)):
        line = ''
        for j in range(0, LINE_LENGTH):
            line += '#' if j in sprite else '.'
            x = cycles[current_cycle]
            sprite = [x - 1, x, x + 1]
            current_cycle += 1
        print(line)

def main():
    file = open('./day_10/input', 'r')
    lines = file.readlines()

    total_cycles, cycles = get_cycles(lines)
    print_lines(total_cycles, cycles)

if __name__ == "__main__":
    main()
