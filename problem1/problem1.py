elvesList = []
current_calories = 0

with open("input.txt") as file:
    for line in file:
        if(line == "\n"):
            elvesList.append(current_calories)

            current_calories = 0
        else:
            current_calories += int(line)

elvesList.sort(reverse=True)
print(f"The elf holding the largest amount of calories holds: {elvesList[0]} calories.")