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


# part 1
# state = (head, tail)
# head = (x,y)
# tail = (x,y)

# part 2
# state = (head=1, 2, 3, .., N=tail)

def step(direction, state):
    head = state[0]
    if direction == "R":
        head = (head[0]+1, head[1])
    elif direction == "L":
        head = (head[0]-1, head[1])
    elif direction == "U":
        head = (head[0], head[1]-1)
    elif direction == "D":
        head = (head[0], head[1]+1)
    state[0] = head
    # 'pull' along the rest of the rope
    for i in range(len(state)-1):
        head, tail = state[i], state[i+1]
        new_tail = follow_tail(head, tail)
        if new_tail == tail:
            break
        state[i+1] = new_tail
    return state

def follow_tail(head, tail):
    if tail[0] == head[0]-2 and tail[1] in (head[1]-1, head[1], head[1]+1):
        tail = (head[0]-1, head[1])
    elif tail[0] == head[0]+2 and tail[1] in (head[1]-1, head[1], head[1]+1):
        tail = (head[0]+1, head[1])
    elif tail[1] == head[1]+2 and tail[0] in (head[0]-1, head[0], head[0]+1):
        tail = (head[0], head[1]+1)
    elif tail[1] ==head[1]-2 and tail[0] in (head[0]-1, head[0], head[0]+1):
        tail = (head[0], head[1]-1)
    elif tail == (head[0]-2, head[1]-2):
        tail = (head[0]-1, head[1]-1)
    elif tail == (head[0]+2, head[1]+2):
        tail = (head[0]+1, head[1]+1)
    elif tail == (head[0]+2, head[1]-2):
        tail = (head[0]+1, head[1]-1)
    elif tail == (head[0]-2, head[1]+2):
        tail = (head[0]-1, head[1]+1)
    return tail

def move(direction, steps, state):
    print("== %s %d ==" %(direction, steps))
    print_state(state)
    for _ in range(steps):
        state = step(direction, state)
        yield state
        print_state(state)
    return state

def symbol(x, y, state):
    if (x,y) not in state:
        return "."
    idx = state.index((x,y))
    if idx == 0:
        return "H"
    elif idx == len(state)-1:
        return "T"
    else:
        return str(idx)

def print_state(state):
    n = 30
    for y in range(n):
        print("".join([symbol(x, y, state) for x in range(n)]))
    print("")

def generate_states(instructions, rope_length=2):
    state = [(15,10)]*rope_length
    for line in instructions:
        direction, steps = line.split()
        for state in move(direction, int(steps), state):
            yield state

# part 1 rope_length=2
# part 2 rope_length=10
rope_length=10
print(len(dict(((tail, 1) for tail in map(itemgetter(-1), generate_states(inputs, rope_length)))).keys()))


