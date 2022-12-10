def is_adjancent(h, t):
    return abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1

def is_tail_adjacent(ti, t, i):
    if i > 0:
        return is_adjancent(ti, t[i - 1])
    return False

def get_next(ti, d, i, t):
    if is_tail_adjacent(ti, t, i):
        return ti
    return [ti[0] + d[0], ti[1] + d[1]]

def get_tail(h, t, prev_h, visited):
    if is_adjancent(h, t[0]):
        return t
    d = [prev_h[0] - t[0][0], prev_h[1] - t[0][1]]
    t.insert(0, prev_h)
    t = [get_next(ti, d, i, t) for i, ti in enumerate(t)]
    if len(t) > 9:
        visited.add(f'{t.pop()}')
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
        t = get_tail(h, t, prev_h, visited)
    return h, t

def main():
    file = open('./day_9/input_sample', 'r')
    lines = file.readlines()

    h = [0,0]
    t = [[0,0]]

    visited = set()

    for line in lines:
        d, n = line.strip().split(' ')
        h, t = move(h, t, int(n), d, visited)
    print(f'** Total: {len(visited)}')

if __name__ == "__main__":
    main()
