def calories_count():
    max_calories = 0
    max_calories_elf = 1
    current_calories = 0
    current_elf = 1
    file = open('input', 'r')
    lines = file.readlines()
    lines.append('\n')

    for line in lines:
        if line.strip():
            current_calories += int(line)
        else:
            if current_calories > max_calories:
                max_calories = current_calories
                max_calories_elf = current_elf
            current_elf += 1
            current_calories = 0

    print(f'* Max calories: {max_calories}')
    print(f'* Elf: {max_calories_elf}')

if __name__ == "__main__":
    calories_count()
