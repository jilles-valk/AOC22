f = open("01_input.txt")
calories = [[]]

elf = 0
lines = f.read()
split = lines.split("\n")
for line in split:
    if not line.isdecimal():
        elf += 1
        calories.append([])
    else:
        calories[elf].append(int(line))

top_three = [0]
for elf in calories:
    total = sum(elf)
    if top_three[0] < total:
        top_three.append(total)
    top_three.sort()
    if len(top_three) > 3:
        top_three.pop(0)
print(top_three)
print(sum(top_three))
