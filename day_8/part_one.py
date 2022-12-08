def build_grid(lines):
    return [[int(x) for x in list(line.strip())] for line in lines]

def is_visible(i, j, grid):
    tree = grid[i][j]

    if not [n for n in [x[j] for x in grid[:i]] if n >= tree]:
        return True
    if not [n for n in [x[j] for x in grid[i+1:]] if n >= tree]:
        return True
    if not [n for n in grid[i][:j] if n >= tree]:
        return True
    if not [n for n in grid[i][j+1:] if n >= tree]:
        return True
    return False

def main():
    file = open('input', 'r')
    lines = file.readlines()
    grid = build_grid(lines)
    num_columns = len(grid[0])
    num_rows = len(grid)
    visibles = num_columns * num_rows - ((num_columns - 2) * (num_rows - 2))

    for i in range(1, num_rows - 1):
        for j in range(1, num_columns - 1):
            if is_visible(i, j, grid):
                visibles += 1
    print(f'** Total: {visibles}')

if __name__ == "__main__":
    main()
