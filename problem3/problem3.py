# We need an ord function that translates 'a' through 'z' to 1~26,
# and 'A' through 'Z' to 27~52

# Get the length of each rucksack and divide it by two. Then 
# go through the fist compartment and check if each individual
# item we come across exists in the second compartment or not
# if yes, add its priority score (1~52) to an overall tracker

# Important: forgot to make a list to keep track of characters
# I've already processed in a line. So if  the character 'R' 
# appeared thrice in the left compartment as well as at least
# once in the right compartment, it would count the value
# thrice. So I added an "already processed" list that resets
# on each iteration

def getPriorityValue(_item):
    if(_item.isupper() ):
        return (ord(_item) - 38)
    else:
        return (ord(_item) - 96)

def getCompartmentContents(_rucksack, _comp_size):
    comp_left_start = 0
    comp_left_end = _comp_size
    comp_right_start = _comp_size
    comp_right_end = (comp_size * 2)

    comp_left = _rucksack[comp_left_start:comp_left_end]
    comp_right = _rucksack[comp_right_start:comp_right_end]
    return (comp_left, comp_right)

with open('input.txt') as file:
    score = 0
    for line in file:
        i = 0
        comp_size = int(len(line) / 2);
        comp_left, comp_right = getCompartmentContents(line, comp_size)
        processed = []

        while(i < comp_size):
            if(comp_left[i] in comp_right):
                if(comp_left[i] not in processed):
                    processed.append(comp_left[i])
                    score += getPriorityValue(comp_left[i])
            i += 1
print(f"Final score: {score}")
