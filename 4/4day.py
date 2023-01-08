import fileinput


lines = list(fileinput.input())
results = []
for line in lines:
    results.append(line)


# Part 1
total = 0
for line in results:
    elf_1, elf_2 = line.strip().split(',')
    min_1, max_1 = map(int, elf_1.split('-'))
    min_2, max_2 = map(int, elf_2.split('-'))
    if ((min_1 <= min_2) and (max_1 >= max_2)) or ((min_1 >= min_2) and (max_1 <= max_2)):
        total += 1

print(total)


# Part 2
total_2 = 0
for line in results:
    elf_1, elf_2 = line.strip().split(',')
    min_1, max_1 = map(int, elf_1.split('-'))
    min_2, max_2 = map(int, elf_2.split('-'))
    if ((min_1 >= min_2) and (min_1 <= max_2)):
        total_2 += 1
    elif ((max_1 >= min_2) and (max_1 <= max_2)):
        total_2 += 1
    elif ((min_1 <= min_2) and (max_1 >= max_2)):
        total_2 += 1

print(total_2)
