# advent of code day 9 - Rope Bridge

from operator import itemgetter

inputs = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()


# state = (head, tail)
# head = (x,y)
# tail = (x,y)

def step(direction, state):
    head, tail = state
    if direction == "R":
        head = (head[0]+1, head[1])
        if tail[0] == head[0]-2:
            tail = (head[0]-1, head[1])
    elif direction == "L":
        head = (head[0]-1, head[1])
        if tail[0] == head[0]+2:
            tail = (head[0]+1, head[1])
    elif direction == "U":
        head = (head[0], head[1]-1)
        if tail[1] == head[1]+2:
            tail = (head[0], head[1]+1)
    elif direction == "D":
        head = (head[0], head[1]+1)
        if tail[1] ==head[1]-2:
            tail = (head[0], head[1]-1)
    return (head, tail)
        
def move(direction, steps, state):
    print("== %s %d ==" %(direction, steps))
    print_state(state)
    for _ in range(steps):
        state = step(direction, state)
        yield state
        print_state(state)
    return state

def symbol(x, y, state):
    head, tail = state
    if (x, y) == head:
        return "H"
    elif (x, y) == tail:
        return "T"
    else:
        return "."

def print_state(state):
    n = 5
    for y in range(n):
        print("".join([symbol(x, y, state) for x in range(n)]))
    print("")

def generate_states(instructions):
    state = ((0,4), (0,4))
    for line in instructions:
        print(line)
        direction, steps = line.split()
        for state in move(direction, int(steps), state):
            yield state
            
print(len(dict(((tail, 1) for tail in map(itemgetter(1), generate_states(inputs)))).keys()))

