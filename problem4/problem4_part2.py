# Import each line, each line represents a range of section IDs (1-100)
# example: 1-20,8-17
# Split the string, separating it by the comma to end up with two groups
# after which we can split the two individual groups to get a begin and
# end value for each ranges they've been assigned:
# Group1: 1 and 20
# Group2: 8 and 17
#
# Sort [TO BE CONTINUED__>>>]

def getOverlap(_range_one, _range_two):
    r1_start =  int(_range_one[0])
    r1_end =    int(_range_one[1])
    r2_start =  int(_range_two[0])
    r2_end =    int(_range_two[1])
    overlap = 0
    
    # Grab however many sections we're overlapping (max - min = overlap)
    if(r1_start <= r2_start and r1_end >=r2_end):
        overlap = (r2_end - r2_start)
    elif(r2_start <= r1_start and r2_end >= r1_end):
        overlap = (r1_end - r1_start)
    
    return overlap

def splitRange(_range):
    return _range.split('-')

def splitGroups(_group):
    return _group.split(',')

def processLine(_line):
    group1, group2 = splitGroups(_line)

    range1 = splitRange(group1)
    range2 = splitRange(group2)

    overlap = getOverlap(range1, range2)

    return overlap

with open("input.txt", 'r') as file:
    overlap = 0
    for line in file:
        overlap += processLine(line)
    
    print(overlap)