import fileinput


lines = list(fileinput.input())
results = []
for line in lines:
    results.append(line)


# Part 1

## Parse input
stacks = [[] for i in range(10)]
for line in results[:8]:
    for i in range(9):
        if ' ' != line[1+i*4]:
            stacks[i+1].insert(0,line[1+i*4])

## Move crates
for step in results[10:]:
    [ _, count, _, start, _, end ] = step.split(' ')
    count, start, end = map(int, [ count, start, end ])
    while count > 0:
        try:
            stacks[end].append(stacks[start].pop())
            count -= 1
        except:
            break

## Print results
for stack in stacks[1:]:
    print(stack.pop(),end='')
print()


# Part 2
## Parse input
stacks = [[] for i in range(10)]
for line in results[:8]:
    for i in range(9):
        if ' ' != line[1+i*4]:
            stacks[i+1].insert(0,line[1+i*4])

## Move crates
for step in results[10:]:
    [ _, count, _, start, _, end ] = step.split(' ')
    count, start, end = map(int, [ count, start, end ])
    pickup = min(count, len(stacks[start]))
    crane = stacks[start][-pickup:]
    stacks[start][-pickup:] = []
    stacks[end].extend(crane)

## Print results
for stack in stacks[1:]:
    print(stack.pop(),end='')
