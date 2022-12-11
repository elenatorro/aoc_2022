def get_cycles(lines):
    CYCLES = [20, 60, 100, 140, 180, 220]
    x = 1
    next_cycle = 0
    cycles = {}
    total = 0

    for line in lines:
        i = line.strip().split()
        c, value = (2, int(i[1])) if i[0] == 'addx' else (1, 0)

        for i in range(next_cycle, next_cycle + c):
            if i not in cycles:
                cycles[i] =  cycles[i - 1] if i > 2 else 1
            if i in CYCLES:
                total += i * cycles[i]

        next_cycle = next_cycle + c
        x = x + value
        cycles[next_cycle] = x
    return total

def main():
    file = open('./day_10/input', 'r')
    lines = file.readlines()
    total = get_cycles(lines)

    print(f'** Total: {total}')

if __name__ == "__main__":
    main()
