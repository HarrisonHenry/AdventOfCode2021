import re
coordinates = [0,0,0]
with open('Day2input.txt') as rawInput:
    data = []
    data = rawInput.readlines()
    commands = []
    for i in data:
        commands.append(i.replace("\n", ""))

for i in commands:
    if (re.search("forward", i)):
        coordinates[0] += int(i[8:])
        coordinates[1] += int(i[8:]) * coordinates[2]
    if (re.search("down", i)):
        coordinates[2] += int(i[5:])
    if (re.search("up", i)):
        coordinates[2] -= int(i[3:])
print(coordinates)
print(coordinates[0] * coordinates[1])
