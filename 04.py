import re

f = open("04_input.txt")
lines = f.readlines()

fully_containing = 0
overlapping = 0
for line in lines:
    a, b, c, d = [int(c) for c in re.split(r"-|,", line[:-1])[:4]]
    if (a >= c and b <= d) or (c >= a and d <= b):
        fully_containing += 1
    if (a >= c and a <= d) or (c >= a and c <= b):
        overlapping += 1

print("04_a: ", str(fully_containing))
print("04_b: ", str(overlapping))