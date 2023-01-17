import fileinput

lines = list(fileinput.input())
results = []
for line in lines:
        results.append(line)

# Part 1

counter = 1
cycle = 1
signal = 0  # Counter x Cycle at various points
instructions = []
closed = 0
while True:
    if not closed:
        try:
            line = results.pop(0)
            match line.strip().split(' '):
                case command, amount:
                    instructions.append((1,int(amount)))
                    closed = 1
        except:
            break
    if (cycle == 20) or ((cycle - 20) % 40 == 0):
        signal += counter * cycle
    if len(instructions) != 0 and instructions[0][0] == 0:
        i = instructions.pop(0)
        counter += i[1]
        closed = 0
    instructions = list(map(lambda a: (a[0]-1, a[1]), instructions))
    cycle += 1

print(signal)


# Part 2

