import fileinput

lines = list(fileinput.input())
results = []
for line in lines:
    results.append(line)

class Tree(object):
    
    def __init__(self, size=0, visible=0, left_vis=0, right_vis=0, 
                 up_vis=0, down_vis=0, score=0):
        self.size = size
        self.visible = visible
        self.left_vis = left_vis
        self.right_vis = right_vis
        self.up_vis = up_vis
        self.down_vis = down_vis
        self.score = score


    def __str__(self):
        return f'(Size: {self.size}, L: {self.left_vis}, R: {self.right_vis}, U: {self.up_vis}, D: {self.down_vis}, Score: {self.score})'

    def __repr__(self):
        return str(self)


# Part 1

def update_visibility(forest):
    for row in forest:
        largest_tree = -1
        for tree in row:
            if tree.size > largest_tree:
                tree.visible = 1
                largest_tree = tree.size
        largest_tree = -1
        for tree in reversed(row):
            if tree.size > largest_tree:
                tree.visible = 1
                largest_tree = tree.size

def count_visible(forest):
    total = 0
    for row in forest:
        for tree in row:
            if tree.visible == 1:
                total += 1
    return total

forest = []
for line in results:
    row = []
    for size in line.strip():
        row.append(Tree(int(size)))
    forest.append(row)

transposed = list(zip(*forest))

update_visibility(forest)
update_visibility(transposed)
print(count_visible(forest))


# Part 2

def update_vis(forest):
    transposed = list(zip(*forest))
    for row in forest:
        for i, tree in enumerate(row):
            j = i
            while j-1 >= 0:
                tree.left_vis += 1
                if row[j-1].size >= tree.size:
                    break
                j -= 1
            while i+1 < len(row):
                tree.right_vis += 1
                if row[i+1].size >= tree.size:
                    break
                i += 1
    for row in transposed:
        for i, tree in enumerate(row):
            j = i
            while j-1 >= 0:
                tree.up_vis += 1
                if row[j-1].size >= tree.size:
                    break
                j -= 1
            while i+1 < len(row):
                tree.down_vis += 1
                if row[i+1].size >= tree.size:
                    break
                i += 1

def update_score(forest):
    for row in forest:
        for tree in row:
            tree.score = tree.left_vis * tree.right_vis * tree.up_vis * tree.down_vis

def find_max_score(forest):
    max_score = 0
    for row in forest:
        for tree in row:
            if tree.score > max_score:
                max_score = tree.score
    return max_score

update_vis(forest)
update_score(forest)
print(find_max_score(forest))
