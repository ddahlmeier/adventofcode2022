from operator import itemgetter

inputs = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def parse_drawing(inputs):
    crates, instructions = inputs.split("\n\n")
    n = len(crates.splitlines()[-1].split())
    stacks = [[line[(4*i)+1:(4*i)+2] for line in crates.splitlines()[:-1]] for i in range(n)]
    stacks = [list(filter(lambda x:x!= ' ', stack)) for stack in stacks]
    return stacks, instructions.splitlines()

def parse_instruction(line):
    n, source, target = list(map(int, itemgetter(1, 3, 5)(line.split())))
    return n, source, target

def move_part1(n, source, target, stacks):
    pick = stacks[source-1][:n]
    stacks[source-1] = stacks[source-1][n:]
    stacks[target-1] = list(reversed(pick)) + stacks[target-1]
    return stacks

def move_part2(n, source, target, stacks):
    pick = stacks[source-1][:n]
    stacks[source-1] = stacks[source-1][n:]
    stacks[target-1] = pick + stacks[target-1]
    return stacks

stacks, instructions = parse_drawing(inputs)
for line in instructions:
    print(stacks)
    print(line)
    n, source, target = parse_instruction(line)
    stacks = move_part2(n, source, target, stacks)
    print("----")

top_crates = ''.join([stack[0] stacks, instructions = parse_drawing(inputs)
for line in instructions:
    print(stacks)
    print(line)
    n, source, target = parse_instruction(line)
    stacks = move_part2(n, source, target, stacks)
    print("----")

stacks, instructions = parse_drawing(inputs)
for line in instructions:
    print(stacks)
    print(line)
    n, source, target = parse_instruction(line)
    stacks = move_part2(n, source, target, stacks)
    print("----")

top_crates = ''.join([stack[0] if len(stack)>0 else ' ' for stack in stacks])

