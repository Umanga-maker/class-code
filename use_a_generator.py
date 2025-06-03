events = [("learn", 5), ("learn", 10), ("relaxed", 20)]
minutes_studied = 0
for event in events:
    if event[0] == "learn":
        minutes_studied += event[1]
print(minutes_studied)

# Think lazy! Use a generator
study_times = (event[1] for event in events if event[0] == "learn")
minutes_studied = sum(study_times)
print(minutes_studied)

# when we use a generator objects are consumed
minutes_studied = sum(study_times)
print(minutes_studied)
