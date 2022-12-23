# Import each line, each line represents a range of section IDs (1-100)
# example: 8-17,1-20
# Split the string, separating it by the comma to end up with two groups
# after which we can split the two individual groups to get a begin and
# end value for each ranges they've been assigned:
# Group1: 8 and 17
# Group2: 1 and 20
#
# Sort the groups based on which sections they're cleaning, in the above
# example, we'd end up with the following after sorting:
# #1: Group2: 1 through 20
# #2: Group1: 8 through 17

def getOverlap(_range_one, _range_two):
    r1_start =  int(_range_one[0])
    r1_end =    int(_range_one[1])
    r2_start =  int(_range_two[0])
    r2_end =    int(_range_two[1])
    overlap = 0

    # Grab however many sections we're overlapping (max - min = overlap)
    overlap = r2_end - r1_start

    return overlap

def splitRange(_range):
    # Return a list of ints (by mapping string to ints)
    return list(map(int, _range.split('-')))

def splitGroups(_group):
    return _group.strip().split(',')

def processLine(_line):
    overlap = 0
    start, end = 0, 1
    group1, group2 = splitGroups(_line)
    range1 = splitRange(group1)
    range2 = splitRange(group2)

    # "Sort" the two groups so we have them sorted on whoever
    # starts at the lowest value to the highest value
    if(range2[start] < range1[start]):
        tmp = range2
        range2 = range1
        range1 = tmp

    if(range1[start] <= range2[end] and range1[end] >= range2[start]):
        overlap = 1

    return overlap

with open("input.txt", 'r') as file:
    overlap = 0
    for line in file:
        overlap += processLine(line)

    print(overlap)