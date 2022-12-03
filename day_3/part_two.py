def reorganize():
    total = 0
    file = open('input', 'r')
    lines = file.readlines()
    groups = zip(*(iter(lines),) * 3)
    for group in groups:
      item = [i for i in group[0] if i in group[1] and i in group[2]][0]
      item = ord(item) - 96 if item.islower() else ord(item) - 38        
      total += item
    print(f'** {total}')

if __name__ == "__main__":
    reorganize()
