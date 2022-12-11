def main():
    file = open('./day_10/input_sample', 'r')
    lines = file.readlines()
    CYCLES = [20, 60, 100, 140, 180, 220]
    x = 1
    next_cycle = 0
    cycles = {}
    total = 0

    for line in lines:
        i = line.strip().split()
        c, value = (2, int(i[1])) if i[0] == 'addx' else (1, 0)
        next_cycle = next_cycle + c
        x = x + value
        cycles[next_cycle] = x

    for c in range(1, next_cycle):
        if c not in cycles:
            cycles[c] = cycles[c - 1] if c > 2 else 1
        if c in CYCLES:
            total += c * cycles[c]

    print(f'** Total: {total}')

if __name__ == "__main__":
    main()
