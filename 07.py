class Node():
    is_dir = False
    name = ""
    size = 0
    children = []
    parent = None

    def __init__(self, parent, name: str, is_dir: bool, size: int = 0, commands: list = None) -> None:
        self.parent = parent
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.children = []
        self.execute_commands(commands)

    def execute_commands(self, commands : list):
        if commands == None or len(commands) == 0:
            return True
        if commands[0][:4] == "$ cd":
            dir = commands[0][5:].strip()
            if dir == "..":
                self.parent.execute_commands(commands[1:])
            elif dir == "/":
                if self.name == "/":
                    self.execute_commands(commands[1:])
                else:
                    self.parent.execute_commands(commands)
            else:
                child  = next(x for x in self.children if x.name == dir)
                if child:
                    child.execute_commands(commands[1:])
                else:
                    self.children.append(Node(self, dir, True, 0, commands[1:]))
        elif commands[0][0:4] == "$ ls":
            i = 1
            while i < len(commands) and commands[i][0] != "$":
                if str(commands[i]).startswith("dir"):
                    self.children.append(Node(self, commands[i][4:].strip(), True))
                else:
                    s, n = commands[i].split(" ")
                    self.children.append(Node(self, n.strip(), False, int(s)))
                i += 1
            commands = commands[i:]
            self.execute_commands(commands)

    def set_size(self):
        if self.is_dir:
            self.size = sum([child.set_size() for child in self.children]) 
        return self.size

    def get_dirs(self) -> list:
        dirs = []
        if not self.is_dir:
            return dirs
        dirs.append(self)
        for child in self.children:
            dirs += child.get_dirs()
        return dirs

    def print_tree(self, depth: int):
        line = " " * depth * 2 + self.name + " ("
        if self.is_dir:
            line += "dir, "
        else:
            line += "file, "
        line += str(self.size) +")"
        print(line)
        for child in self.children:
            child.print_tree(depth + 1)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self):
        return self.__str__()

f = open("07_input.txt")
commands = f.readlines()

node = Node(None, "/", True, 0, commands)
node.set_size()
dirs = node.get_dirs()
sum_above_hk = sum([dir.size for dir in dirs if dir.size < 100000])

node.print_tree(0)
print("07_a: " + str(sum_above_hk))

available = 70000000 - node.size
smallest = node
for dir in dirs:
    if dir.size + available > 30000000 and dir.size < smallest.size:
        smallest = dir

print("07_b: " + str(smallest.size))