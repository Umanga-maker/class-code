lines = ["line1", "line2", "line3", "line4", "line5", "line6", "line7","line8", "line9","line10",]
for i, line in enumerate(lines):
    if i >=5:
        break
    print(line)

print()

# Using islice
from itertools import islice

first_five_lines = islice(lines, 1, 6, 2)#ranges are from indexes of lines
for line in first_five_lines:
    print(line)
