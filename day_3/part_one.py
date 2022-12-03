def reorganize():
    total = 0
    file = open('input', 'r')
    lines = file.readlines()
    for line in lines:
        half = int(len(line) / 2)
        r1, r2 = line[:half], line[half:]
        item = [i for i in r1 if i in r2][0]
        item = ord(item) - 96 if item.islower() else ord(item) - 38
        total += item
    print(f'** {total}')
  
if __name__ == "__main__":
    reorganize()
