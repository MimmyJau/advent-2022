import fileinput


lines = list(fileinput.input())
results = []
for line in lines:
    results.append(line)


def get_char_value(char):
    if ord(char) >= ord('a'):
        return ord(char)-ord('a')+1
    else:
        return ord(char)-ord('A')+26+1


# Part 1
priority = 0
for line in results:
    length = int(len(line.strip())/2)
    comp_1 = set(line[:length])
    comp_2 = set(line[length:])
    inter = ''.join(comp_1.intersection(comp_2))
    priority += get_char_value(inter)

print(priority)


# Part 2
total = 0
for i in range(0,len(results),3):
    elf_1 = set(results[i].strip())
    elf_2 = set(results[i+1].strip())
    elf_3 = set(results[i+2].strip())
    badge = ''.join(elf_1.intersection(elf_2.intersection(elf_3)))
    total += get_char_value(badge)

print(total)


