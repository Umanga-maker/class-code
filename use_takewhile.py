for item in [1,2,3,-1,5,-4,9]:
    if item >= 0:
        print(item)
    else:
        break

print()

# Using takewhile
from itertools import takewhile
items = takewhile(lambda x:x >= 0, [1,2,3,-1,5,-4,9])
for item in items:
    print(item)