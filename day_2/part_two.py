def play_game():
    score = 0
    file = open('input', 'r')
    lines = file.readlines()

    scores_choice = {
        'AX': 3,
        'AY': 1,
        'AZ': 2,
        'BX': 1,
        'BY': 2,
        'BZ': 3,
        'CX': 2,
        'CY': 3,
        'CZ': 1
    }

    scores_match = {
        'AX': 0,
        'AY': 3,
        'AZ': 6,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 0,
        'CY': 3,
        'CZ': 6
    }

    for line in lines:
        (score_a, score_b) = line.strip().split(' ')
        score += scores_choice[score_a + score_b] + scores_match[score_a + score_b]
    print(f'* Score: {score}')
  
if __name__ == "__main__":
    play_game()
