import re

f = open("05_input.txt")
lines = f.readlines()
stacks = []

i = 0
while lines[i] != "\n":
    i += 1
max_height = i - 2
num_stacks = int(re.search(r"\d+ $", lines[i - 1]).group())

for i in range(num_stacks):
    stacks.append([])
    for j in range(max_height, -1, -1):
        item = lines[j][4 * i + 1]
        if item != " ":
            stacks[i].append(item)

stacks_b = [stack.copy() for stack in stacks]
move_instructions_start = max_height + 3
for i in range(move_instructions_start, len(lines)):
    c, f, t = [int(item) for item in re.findall(r"(\d+)", lines[i])]
    for j in range(c):
        stacks[t - 1].append(stacks[f - 1].pop())
    
    stacks_b[t - 1] = stacks_b[t - 1] + stacks_b[f - 1][-c:]
    stacks_b[f - 1] = stacks_b[f - 1][:-c]

print("05_a: " + "".join([stack[-1] for stack in stacks]))
print("05_b: " + "".join([stack[-1] for stack in stacks_b]))