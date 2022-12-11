# A - X -- Rock
# B - Y -- Paper
# C - Z -- Scissors


def winOrLose(_input1, _input2):
    tmp_score = 0

    if _input2 == "X":
        tmp_score = 1

        if _input1 == "A":
            # Draw (Rock vs Rock)
            tmp_score += 3
        elif _input1 == "B":
            # Rock is defeated by Paper, we lose
            tmp_score += 0
        elif _input1 == "C":
            # Rock beats Scissors, we win
            tmp_score += 6
    elif _input2 == "Y":
        tmp_score = 2

        if _input1 == "A":
            # Paper defeats Rock, we win
            tmp_score += 6
        elif _input1 == "B":
            # Draw (Paper vs Paper)
            tmp_score += 3
        elif _input1 == "C":
            # Paper is defeated by scissors, we lose
            tmp_score += 0
    elif _input2 == "Z":
        tmp_score = 3

        if _input1 == "A":
            # Scissors is defeated by Rock, we lose
            tmp_score += 0
        elif _input1 == "B":
            # Scissors defeats Paper, we win
            tmp_score += 6
        elif _input1 == "C":
            # Draw (Scissors vs Scissors)
            tmp_score += 3

    return tmp_score


score = 0
with open("input.txt") as file:
    for line in file:
        input = line.strip().split(" ")
        score += winOrLose(input[0], input[1])
        print(f"Score of this move: {winOrLose(input[0], input[1])}\n")
print("Score: " + str(score))