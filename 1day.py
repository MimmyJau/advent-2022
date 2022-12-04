import fileinput


lines = list(fileinput.input())
results = []
for line in lines:
    results.append(line)


# Part 1
index = 0
total = 0
calories = []
for line in results:
    if line == '\n':
        calories.append(total)
        index += 1
        total = 0
    else:
        total += int(line)

print(max(calories))


# Part 2
calories.sort(reverse=True)
print(sum(calories[:3]))
