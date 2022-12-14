# We need an ord function that translates 'a' through 'z' to 1~26,
# and 'A' through 'Z' to 27~52

# Iterate through the file as usual, but instead of processing it line
# by line, store each rucksack by appending them into a list, a list that
# will hold up to 3 strings at any given time. Each time we've collected
# 3 rucksacks we process them before clearing the list and processing the
# next 3 elves (lines)

# Then process the items one by one from that newly made string, check
# to see if an item is present in all 3 bags or not, if yes, that's the
# identifying badge we're looking for! Add it to the score.

def getPriorityValue(_item):
    if(_item.isupper() ):
        return (ord(_item) - 38)
    else:
        return (ord(_item) - 96)

def processRucksacks(_rucksacks):
    # Get the contents of each bag without duplicate characters
    rsack1 = "".join(set(_rucksacks[0]))
    rsack2 = "".join(set(_rucksacks[1]))
    rsack3 = "".join(set(_rucksacks[2]))

    i = 0
    score = 0
    while(i < len(rsack1)):
        # If the item is also in both rucksack 2 and 3
        if( rsack1[i] in rsack2 and rsack1[i] in rsack3):
            score += getPriorityValue(rsack1[i])

        i += 1 

    return score


with open('input.txt') as file:
    score = 0
    counted_rucksacks = 0
    rucksacks = []

    for line in file:
        # Store the rucksacks until we've stored 3 of them
        rucksacks.append(line.strip())

        counted_rucksacks += 1

        # Once we've got the contents of 3 rucksacks, process them!
        if(counted_rucksacks >= 3):
            score += processRucksacks(rucksacks)

            counted_rucksacks = 0
            rucksacks.clear()

print(f"{score}")

