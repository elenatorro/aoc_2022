def main():
    file = open('./day_10/input', 'r')
    lines = file.readlines()
    x = 1
    next_cycle = 0
    cycles = {}
    LINE_LENGTH = 40

    for line in lines:
        i = line.strip().split()
        c, value = (2, int(i[1])) if i[0] == 'addx' else (1, 0)
        next_cycle = next_cycle + c
        x = x + value
        cycles[next_cycle] = x

    for c in range(1, next_cycle):
        if c not in cycles:
            cycles[c] = cycles[c - 1] if c > 2 else 1

    x = 1
    current_cycle = 1

    for i in range(0, int(next_cycle / LINE_LENGTH)):
        line = ''
        sprite = [x - 1, x, x + 1]
        for j in range(0, LINE_LENGTH):
            line += '#' if j in sprite else '.'
            x = cycles[current_cycle]
            sprite = [x - 1, x, x + 1]
            current_cycle += 1
        print(line)

if __name__ == "__main__":
    main()
