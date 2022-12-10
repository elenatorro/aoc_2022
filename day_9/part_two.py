def is_adjancent(h, t):
    return abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1

def is_adjacent_horizontal(h, t):
    return abs(h[0] - t[0]) > 1 and abs(h[1] - t[1]) <= 1

def is_adjacent_vertical(h, t):
    return abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) > 1

def get_next_tail(prev_t, ti):
    if is_adjancent(prev_t, ti):
        return ti

    inc_0 = -1 if prev_t[0] > ti[0] else 1
    inc_1 = -1 if prev_t[1] > ti[1] else 1

    if is_adjacent_horizontal(prev_t, ti):
        return [prev_t[0] + inc_0, prev_t[1]]

    if is_adjacent_vertical(prev_t, ti):
        return [prev_t[0], prev_t[1] + inc_1]

    return [prev_t[0] + inc_0, prev_t[1] + inc_1]

def get_tail(t, prev_h, visited):
    t[0] = get_next_tail(prev_h, t[0])
    for i in range(1, len(t)):
        t[i] = get_next_tail(t[i - 1], t[i])
    visited.add(f'{t[-1]}')
    return t

def get_head(h, d):
   if d == 'L':
      return [h[0]-1, h[1]]
   elif d == 'R':
      return [h[0]+1, h[1]]
   elif d == 'U':
      return [h[0], h[1]+1]
   elif d == 'D':
      return [h[0], h[1]-1]

def move(h, t, n, d, visited):
    for i in range(1, n+1):
        prev_h = h
        h = get_head(h, d)
        t = get_tail(t, prev_h, visited)
    return h, t

def main():
    file = open('./day_9/input', 'r')
    lines = file.readlines()

    h = [0,0]
    t = [[0,0] for i in range(9)]

    visited = set()

    for line in lines:
        d, n = line.strip().split(' ')
        h, t = move(h, t, int(n), d, visited)
    print(f'** Total: {len(visited) + 1}')

if __name__ == "__main__":
    main()
