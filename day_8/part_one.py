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
    c = len(grid[0])
    r = len(grid)
    total = (c * r - ((c - 2) * (r - 2))) + sum(map(lambda i: len([j for j in range(1, c - 1) if is_visible(i, j, grid)]), range(1, r - 1)))
    print(f'** Total: {total}')

if __name__ == "__main__":
    main()
