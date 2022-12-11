def getIntValue(_input):
    # Turn A, B, C into 1, 2 and 3
    return (ord(_input)  - 64)

def determineOutcome(_input, shouldWin=True):
    if(_input == "A"): # Rock
        if(shouldWin): return "B"
        else: return "C"
    elif(_input == "B"): # Paper
        if(shouldWin): return "C"
        else: return "A"
    elif(_input == "C"): # Scissor
        if(shouldWin): return "A"
        else: return "B"
    else:
        print("determineOutcome() :: Wrong input received: " + _input)


def determineOurMove(_input, _outcome):
    if _outcome == "X":
        # Get lose result
        return determineOutcome(_input, False)
    elif _outcome == "Y":
        # Get draw result
        return _input
    elif _outcome == "Z":
        # Get win result
        return determineOutcome(_input)

score = 0
ourAction = ""
with open("input.txt") as file:
    for line in file:
        curLine = line.strip().split(" ")
        opponentMove = curLine[0]
        roundConclusion = curLine[1]

        # Give us scores based on the result
        # we're supposed to have
        if(roundConclusion == "Y"):
            # Draw
            score += 3
        elif(roundConclusion == "Z"):
            # Win
            score += 6

        # Determine the move we made and give
        # the appropriate score
        ourAction = determineOurMove(opponentMove, roundConclusion)
        if(ourAction == "A"):
            # We used rock
            score += 1
        elif(ourAction == "B"):
            # We used paper
            score += 2
        else:
            # We used scissor
            score += 3

print("Score: " + str(score))