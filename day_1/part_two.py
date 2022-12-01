def calories_count():
    top_max_calories = []
    current_calories = 0

    file = open('input', 'r')
    lines = file.readlines()
    lines.append('\n')

    for line in lines:
        if line.strip():
            current_calories += int(line)
        else:
            if len(top_max_calories) < 3:
                top_max_calories.append(current_calories)
            else:
                i = next((i for i, max_calories in enumerate(top_max_calories) if current_calories > max_calories), -1)
                if i > -1:
                  top_max_calories[i] = current_calories
            current_calories = 0

    print(f'* Max calories: {top_max_calories}')
    print(f'* Total: {sum(top_max_calories)}')
  
if __name__ == "__main__":
    calories_count()
