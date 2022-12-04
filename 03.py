def get_priorities(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

f = open("03_input.txt")
lines = f.readlines()

priorities = 0
for line in lines:
    l = int(len(line)/2)
    compartment_a = line[0:l]
    compartment_b = line[l:-1]
    in_both = set()
    for i in range(l):
        if compartment_b.__contains__(compartment_a[i]):
            in_both.add(compartment_a[i])
    priorities += sum([get_priorities(c) for c in in_both])

print("03_a: " + str(priorities))

priorities_badge = 0
for i in range(0, len(lines), 3):
    if (i + 2 > len(lines)):
        break
    common = set(lines[i][:-1])
    common = common.intersection(lines[i + 1][:-1])
    common = common.intersection(lines[i + 2][:-1])
    priorities_badge += sum([get_priorities(c) for c in common])

print("03_b: " + str(priorities_badge))