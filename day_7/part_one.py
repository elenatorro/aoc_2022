class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}

    def add_child(self, name):
        if name not in self.children:
            child = Node(name, self)
            self.children[name] = child

    def add_file(self, filename, filesize):
        self.files[filename] = int(filesize)

    def get_total_size(self):
        total = sum([value for value in self.files.values()])
        for child in self.children.values():
            total += child.get_total_size()
        return total

    def get_size_by_child(self, total=None):
        total = total or []
        total.append(self.get_total_size())
        for child in self.children.values():
            child.get_size_by_child(total)
        return total


def parse_file_into_tree(lines):
    tree = Node('/')
    current_node = tree

    for line in lines:
        line = line.strip()
        if '$ ls' in line:
            continue
        elif '$ cd' in line:
            dir = line.split(' ')[2]
            if dir == '..':
                current_node = current_node.parent
            elif dir != '/':
                current_node.add_child(dir)
                current_node = current_node.children[dir]
        elif 'dir' in line:
            current_dir = line.split(' ')[1]
            current_node.add_child(current_dir)
        else:
            filesize, filename = line.split(' ')
            current_node.add_file(filename, filesize)
    return tree


def get_total_values(tree):
    MAX_FILE_SIZE = 100000

    total = tree.get_size_by_child()
    return sum([v for v in total if v <= MAX_FILE_SIZE])


def main():
    file = open('input', 'r')
    lines = file.readlines()

    tree = parse_file_into_tree(lines)
    total = get_total_values(tree)

    print(f'** Total: {total}')


if __name__ == "__main__":
    main()
