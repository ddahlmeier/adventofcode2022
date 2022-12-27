# advent of code 2022 day 7 - no space left on device 

from collections import defaultdict

inputs = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()



def parse_inputs(inputs):
    mode = ""
    sub_directories = defaultdict(list)
    file_sizes = {}
    working_dir = []
    for line in inputs:
        if line.startswith("$"):
            if line.startswith("$ cd"):
                # process commands: ls, cd
                _, _, arg = line.split()
                if arg == "..":
                    working_dir.pop()
                elif arg == "/":
                    working_dir = []
                else:
                    working_dir.append(arg)
            elif line.startswith("$ ls"):
                mode = "ls"
        elif mode == "ls":
            cwd = "/".join(working_dir)
            # list directory
            if line.startswith("dir"):
                _, directory = line.split()
                sub_directories[cwd].append(directory)
            else:
                size, filename = line.split()
                file_sizes[cwd + "/" + filename] = int(size)
    return sub_directories, file_sizes


def total_directory_sizes(file_sizes):
    dir_sizes = defaultdict(int)
    for file, size in file_sizes.items():
        path = file.split("/")
        for i in range(len(path)):
            dir_sizes["/".join(path[:i])] += size
    return dir_sizes

tree, sizes = parse_inputs(inputs)
# part 1
dir_sizes = total_directory_sizes(sizes)
print(sum(filter(lambda x:x<=100000, dir_sizes.values())))

# part 2
total_disk_size = 70000000
needed_disk_space = 30000000
free_disk = total_disk_size - dir_sizes['']
print(list(filter(lambda x:x[1]+free_disk >= needed_disk_space, sorted(dir_sizes.items(), key=itemgetter(1))))[0])

