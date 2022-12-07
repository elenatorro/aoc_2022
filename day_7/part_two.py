class Node:
    def __init__(self, uid, name, parent=None):
        self.uid = uid
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}

    def add_child(self, uid, name):
        child = Node(uid, name, self)
        self.children[name] = child

    def add_file(self, filename, filesize):
        self.files[filename] = int(filesize)

    def get_total_size(self):
        total = sum([value for value in self.files.values()])
        for child in self.children.values():
            total += child.get_total_size()
        return total

    def get_size_by_child(self, total=None):
        total = total or {}
        total.update({
            f'{self.uid}_{self.name}': self.get_total_size()
        })
        for child in self.children.values():
            child.get_size_by_child(total)
        return total


def main():
    MAX_DISK_SPACE = 70000000
    MAX_UNUSED_DISK_SPACE = 30000000

    file = open('input', 'r')
    lines = file.readlines()
    tree = Node(0, '/')
    uids = 1

    current_node = tree
    current_dir = None

    for line in lines:
        line = line.strip()
        line_parts = line.split(' ')
        if line_parts[0] == '$':
            if line_parts[1] == 'cd' and line_parts[2] != '/':
                if line_parts[2] == '..':
                    current_node = current_node.parent
                else:
                    if line_parts[2] not in current_node.children:
                        current_node.add_child(uids, line_parts[2])
                        uids += 1
                    current_node = current_node.children[line_parts[2]]
        elif line_parts[0] == 'dir':
            current_dir = line_parts[1]
            if current_dir not in current_node.children:
                current_node.add_child(uids, current_dir)
                uids += 1
        else:
            current_node.add_file(line_parts[1], line_parts[0])
    total = tree.get_size_by_child()
    unused_space = MAX_DISK_SPACE - total['0_/']
    min_disk_space = MAX_UNUSED_DISK_SPACE - unused_space
    total_space = sorted([v for v in total.values() if v >= min_disk_space])[0]
    print(f'** Total: {total_space}')


if __name__ == "__main__":
    main()