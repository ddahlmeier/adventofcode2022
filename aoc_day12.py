# Advent of code 12: Hill Climbing Algorithm

from itertools import product
from collections import defaultdict

inputs = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

def height(symbol):
    if symbol == "S":
        return ord('a')
    elif symbol == "E":
        return ord("z")
    else:
        return ord(symbol)

def is_accessible(start, end):
    return height(start)+1 >= height(end)

def neighbors(row, column, map_dim):
    if row > 0:
        yield (row-1, column)
    if row < map_dim[0]-1:
        yield (row+1, column)
    if column > 0:
        yield (row, column-1)
    if column < map_dim[1]-1:
        yield (row, column+1)
    
def parse_map(map):
    adjacency = defaultdict(list)
    map_dim = (len(map), len(map[0])) 
    start = None
    end = None
    for row, line in enumerate(map):    
        for column, symbol in enumerate(line):
            if symbol == "S":
                start = (row, column)
            if symbol == "E":
                end = (row, column)
            for neighbor in neighbors(row, column, map_dim):
                if is_accessible(symbol, map[neighbor[0]][neighbor[1]]):
                    adjacency[(row,column)].append(neighbor)
    return adjacency, start, end, map_dim


def in_queue(queue, node, distance):
    for n, d in queue:
        if n == node and d <= distance:
            return True
    return False

def starting_points(map):
    for row, line in enumerate(map):
        for column, symbol in enumerate(line):
            if height(symbol) == height('a'):
                yield (row, column)

def bfs(map, single_start=True):
    adjacency, start, end, map_dim = parse_map(map)
    if single_start:
        queue = [(start, 0)]
    else:
        queue = [(node, 0) for node in starting_points(map)]
    explored = defaultdict(bool)
    while len(queue) > 0:
        node, steps = queue.pop(0)
        explored[node] = True
        print("exploring node:", node, " distance: ", steps)
        print_map(map, explored, map_dim)
        if node == end:
            print("found end node")
            break
        for neighbor in adjacency[node]:
            if explored[neighbor] or in_queue(queue, neighbor, steps+1):
                continue
            print("add to queue node:", neighbor, " distance: ", steps+1)
            queue.append((neighbor, steps+1))
            print("queue:", queue)


def print_map(map, explored, map_dim):
    for row in range(map_dim[0]):
        for column in range(map_dim[1]):
            if explored[(row, column)]:
                # print red
                print("\033[91m{}\033[00m" .format(map[row][column]), end="")
            else:
                print(map[row][column], end="")
        print("")

# part 1
map = inputs.splitlines()
bfs(map, single_start=True)

# part 2
bfs(map, single_start=False)
