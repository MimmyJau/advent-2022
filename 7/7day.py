import fileinput

lines = list(fileinput.input())
results = []
for line in lines:
    results.append(line)


class Dirs(object):

    def __init__(self, name, parent=None, children={}, files={}):
        self.name = name
        self.parent = parent
        self.children = children
        self.files = files
        self.size = 0

    def mkdir(self, name):
        temp = Dirs(name, self, children={}, files={})
        self.children[name] = temp

    def new_file(self, name, size=0):
        temp = File(name, size)
        self.files[name] = temp
        # TODO: Only add size of new file
        self.update_size()
    
    def update_size(node):
        while node != None:
            total_size = 0
            for key, file in node.files.items():
                total_size += file.size
            for key, child in node.children.items():
                total_size += child.size
            node.size = total_size
            node = node.parent

    def print(self, indent=""):
        print(indent, self.name, self.size)
        indent =  indent + " "
        for key, children in self.children.items():
            children.print(indent)
        for key, file in self.files.items():
            print(indent, file.name, file.size)
        indent = indent[:-1]


class File(object):

    def __init__(self, name, size=0):
        self.name = name
        self.size = size



# Part 1

root = Dirs('/')
home = root
for line in results:
    tokens = line.strip().split(' ')
    if tokens[0] == '$':
        if tokens[1] == "cd":
            if tokens[2] == "..":
                root = root.parent
            elif tokens[2] == '/':
                root = home
            else:
                root = root.children[tokens[2]]
    elif tokens[0] == "dir":
        if tokens[1] in root.children:
            break
        else:
            root.mkdir(tokens[1])
    else:
        size = int(tokens[0])
        name = tokens[1]
        root.new_file(name, size)


def sum_over_x(root, x):
    total = 0
    for key, child in root.children.items():
        total += sum_over_x(child, x)
    if root.size <= x :
        return root.size + total
    else:
        return total


print(sum_over_x(home, 100000))

# Part 2
available = 70000000 - home.size
required = 30000000
difference = required - available

def dfs_findall(root, lst):
    for key, child in root.children.items():
        lst = dfs_findall(child, lst)
    if root.size >= difference:
        lst.append(root.size)
    return lst

acceptable_dirs = []
acceptable_dirs = dfs_findall(home, acceptable_dirs)
acceptable_dirs.sort()
print(acceptable_dirs)
