def getIntValue(_input):
    return (ord(_input)  - 64)

def determineWeakness(_input):
    if(_input == "A"):
        return "B"
    elif(_input == "B"):
        return "C"
    elif(_input == "C"):
        return "A"
    else:
        print("determineWeakness() :: Wrong input received: " + _input)

def determineResolution(_input1, _input2):
    score = getIntValue(_input2)

    if(_input2 == determineWeakness(_input1)):
        # We win
        score += 6
    elif(_input1 == _input2):
        # Draw
        score += 3
    else:
        # We lose
        score += 0

    return score


score = 0
with open("input.txt") as file:
    for line in file:
        curLine = line.strip().split(" ")
        opponentMove = curLine[0]
        playerMove = curLine[1]

        # Convert the moves to the same character for easy comparison
        if(playerMove == "X"): playerMove = "A"
        elif(playerMove == "Y"): playerMove = "B"
        elif(playerMove == "Z"): playerMove = "C"

        score += determineResolution(opponentMove, playerMove)
print("Score: " + str(score))