"""
ALGORITHM:
1. build a dictionary for scoring
2. read each line from the input file and look up values on the scoring table
3. calculate the scores

"""

scoring_table = {
    "A X\n": 3,
    "A Y\n": 4,
    "A Z\n": 8,
    "B X\n": 1,
    "B Y\n": 5,
    "B Z\n": 9,
    "C X\n": 2,
    "C Y\n": 6,
    "C Z\n": 7,
}


def final_score():
    score = 0
    with open("2_input.txt") as input_file:
        for line in input_file:
            score += scoring_table[line]
    return score


score_of_all_games = final_score()
print(score_of_all_games)
