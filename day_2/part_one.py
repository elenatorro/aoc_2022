def play_game():
    score = 0
    file = open('input', 'r')
    lines = file.readlines()

    scores_choice = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    scores_match = {
        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3
    }

    for line in lines:
        (score_a, score_b) = line.strip().split(' ')
        score += scores_choice[score_b] + scores_match[score_a + score_b]
    print(f'* Score: {score}')
  
if __name__ == "__main__":
    play_game()
