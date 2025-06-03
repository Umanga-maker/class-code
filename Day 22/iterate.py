it = iter([1,2,3,4,5])
print (next(it))
while True:
    try:
        no = next(it)
        print(no)
    except StopIteration:
        break
