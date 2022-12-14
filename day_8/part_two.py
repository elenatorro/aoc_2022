def build_grid(lines):
    return [[int(x) for x in list(line.strip())] for line in lines]

def get_path(tree, path):
    for i, t in enumerate(path):
        if t >= tree:
            break
    return i + 1

def get_score(i, j, grid):
    tree = grid[i][j]

    top = get_path(tree, [x[j] for x in grid[:i]][::-1])
    left = get_path(tree, grid[i][:j][::-1])
    bottom = get_path(tree, [x[j] for x in grid[i+1:]])
    right = get_path(tree, grid[i][j+1:])

    return top * bottom * left * right

def main():
    file = open('input', 'r')
    lines = file.readlines()
    grid = build_grid(lines)
    max_scores = max(map(lambda i: max([get_score(i, j, grid) for j in range(1, len(grid) - 1)]), range(1, len(grid[0]) - 1)))

    print(f'** Max score: {max_scores}')

if __name__ == "__main__":
    main()
