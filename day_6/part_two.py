def packet_signal():
    file = open('input', 'r')
    lines = file.readlines()
    line = list(lines[0])
    prev = []
    while len(set(prev[-14:])) < 14:
        prev.append(line.pop(0))
    print(f'** Total: {len(prev)}')

if __name__ == "__main__":
    packet_signal()
