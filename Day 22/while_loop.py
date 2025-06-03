count = 0
while count < 7:# condition
    print(count)
    count += 1

for c in 'family':
    print(c.capitalize())

fam = [1.45, 1.49, 1.78, 1.96]
for index, height in enumerate(fam):
    print("index" + str(index)+ ": "+ str(height))