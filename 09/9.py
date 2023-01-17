import fileinput

lines = list(fileinput.input())
results = []
for line in lines:
        results.append(line)

# Part 1

head = [0,0]
tail = [0,0]

moveset = { 'U': [0,1], 'D': [0,-1], 'R': [1,0], 'L': [-1,0] }

def update_tail(tail, head):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if (abs(x_diff) < 2) and (abs(y_diff) < 2):
        return tail
    # For Part 2, special case where leading section is
    # diagonal and then it moves diagonally again
    elif (abs(x_diff) == 2) and (abs(y_diff) == 2):
        if x_diff == 2:
            tail[0] += 1
        else:
            tail[0] -= 1
        if y_diff == 2:
            tail[1] += 1
        else:
            tail[1] -= 1
    else:
        if x_diff == 0:
            if y_diff < 0:
                tail[1] -= 1
            else:
                tail[1] += 1
        elif y_diff == 0:
            if x_diff < 0:
                tail[0] -=1 
            else:
                tail[0] += 1
        else:
            if x_diff > 1:
                tail[0] += 1
                tail[1] = head[1]
            elif x_diff < -1:
                tail[0] -= 1
                tail[1] = head[1]
            elif y_diff > 1:
                tail[1] += 1
                tail[0] = head[0]
            elif y_diff < -1:
                tail[1] -= 1
                tail[0] = head[0]
    return tail

record = { 0: {0} }

for move in results:
    direction, size_str = move.strip().split(' ')
    size = int(size_str)
    step = moveset[direction]
    while size > 0:
        head[0] += step[0]
        head[1] += step[1]
        update_tail(tail, head)
        try: 
            record[tail[0]].add(tail[1])
        except:
            record[tail[0]] = { tail[1] }
        size -= 1

total = 0
for key, value in record.items():
    total += len(value)
print(total)


# Part 2
snake = [[0,0] for i in range(10)]
head = snake[0]
tail = snake[-1]
tail_record = { 0: {0} }

for move in results:
    direction, size_str = move.strip().split(' ')
    size = int(size_str)
    step = moveset[direction]
    while size > 0:
        head[0] += step[0]
        head[1] += step[1]
        for i in range(1,10):
            update_tail(snake[i],snake[i-1])
        try: 
            tail_record[tail[0]].add(tail[1])
        except:
            tail_record[tail[0]] = { tail[1] }
        size -= 1

total = 0
for key, value in tail_record.items():
    total += len(value)
print(total)

