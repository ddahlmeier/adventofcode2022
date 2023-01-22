# Advent of Code 14: Regolith Reservoir

from operator import itemgetter

inputs = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

def parse(inputs):
    all_points = []
    for line in inputs:
        last_point = None
        points = []
        for point in line.split(" -> "):
            point = tuple(map(int, point.split(",")))
            if last_point:
                if last_point[0] == point[0] and last_point[1] != point[1]:
                    direction = 1 if point[1] > last_point[1] else -1
                    for y_hat in range(last_point[1], point[1], direction):
                        points.append((point[0], y_hat))
                elif last_point[0] != point[0] and last_point[1] == point[1]:
                    direction = 1 if point[0] > last_point[0] else -1
                    for x_hat in range(last_point[0], point[0], direction):
                        points.append((x_hat, point[1]))
                else:
                    print("next point differs in both x and y")
                    assert(False)
            last_point = point
        points.append(point)
        all_points.extend(points)
    return all_points

def print_map(rocks, sands, entrance, rangex, rangey):
    for y in range(*rangey):
        for x in range(*rangex):
            if (x,y) in rocks:
                symbol = "#"
            elif (x,y) in sands:
                symbol = "o"                            
            elif (x,y) == entrance:
                symbol = "+"
            else:
                symbol = "."
            print(symbol, end="")
        print("")
    
def isblocked(x, y, rocks, sands,  bottom=None):
    if bottom and y == bottom:
        return True
    return (x, y) in rocks or (x, y) in sands

def simulate_step(sand_unit, rocks, sands, bottom=None):
    x, y = sand_unit
    if not isblocked(x, y+1, rocks, sands, bottom):
        return (x, y+1), False
    elif not isblocked(x-1, y+1, rocks, sands, bottom):
        return (x-1, y+1), False
    elif not isblocked(x+1, y+1, rocks, sands, bottom):
        return (x+1, y+1), False
    else:
        return (x, y), True

def simulate(sand, rocks, sands, max_depth, bottom=None):
    blocked = False
    while not blocked:
        sand, blocked = simulate_step(sand, rocks, sands, bottom)
        if blocked:
            sands.append(sand)
            if bottom and sand == (500,0):
                print("entrance is clocked")
                return sands, True
            else:
                return sands, False
        elif bottom == None and sand[1] >= max_depth:
            print("sand falls out the bottom")
            return sands, True
    return sands


# part 1
sands = []
rocks = parse(inputs)
max_depth = max(map(itemgetter(1), rocks))+1
for i in range(1000):
    print("simulate sand unit:", i)
    sands, completed = simulate((500, 0), rocks, sands, max_depth)
    if i % 2 == 0:
        print_map(rocks, sands, (500,0), (420,550), (0,12))
    if completed:
        break

# part 2
sands = []
rocks = parse(inputs)
max_depth = max(map(itemgetter(1), rocks))+2
for i in range(100000):
    sands, completed = simulate((500, 0), rocks, sands, max_depth, bottom=max_depth)
    if i % 1000 == 0:
        print("simulate sand unit:", i)
        print_map(rocks, sands, (500,0), (420,550), (0,170))
    if completed:
        break


