# X = lose
# Y = draw
# Z = win

def getIntValue(_input):
    return (ord(_input)  - 64)

def determineWeakness(_input, shouldWin):
    if(_input == "A"):
        if(shouldWin): return "B"
        else: return "C"
    elif(_input == "B"):
        if(shouldWin): return "C"
        else: return "A"
    elif(_input == "C"):
        if(shouldWin): return "A"
        else: return "B"
    else:
        print("determineWeakness() :: Wrong input received: " + _input)


def determineOurMove(_input1, _outcome):
    if _outcome == "X":
        #
    elif _outcome == "Z"

    return score

score = 0
with open("input.txt") as file:
    for line in file:
        curLine = line.strip().split(" ")
        opponentMove = curLine[0]
        roundConclusion = curLine[1]

        # Convert the moves to the same character for easy comparison
        #if(playerMove == "X"): playerMove = "A"
        #elif(playerMove == "Y"): playerMove = "B"
        #elif(playerMove == "Z"): playerMove = "C"

        if(roundConclusion == "Y"):
            # Draw
            score += 3
        elif(roundConclusion == "Z"):
            # We have to win
            score += 6

        score += determineOurMove(opponentMove, roundConclusion)
#print("Score: " + str(score))


# Print simple tests
