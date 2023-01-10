# Advent of Code 13: Distress Signal

import math
import functools
from operator import itemgetter

inputs = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def parse(line):
    stack = [[]]
    for symbol in line:
        if symbol == "[":
            stack.append([])
        elif symbol == "]":
            if len(stack[-1])>0 and type(stack[-1][-1])==str:
                stack[-1].append(int(stack[-1].pop()))
            completed = stack.pop()
            stack[-1].append(completed)
        elif symbol == ",":
            if len(stack[-1])>0 and type(stack[-1][-1])==str:
                stack[-1].append(int(stack[-1].pop()))
        elif symbol in "0123456789":
            if len(stack[-1])>0 and type(stack[-1][-1]) == str:
                stack[-1][-1] += symbol
            else:            
                stack[-1].append(symbol)
        else:
            print("unexpected symbol:", symbol)
            assert(False)
    return stack[0][0]

def cmp(left, right):
    print("Compare", left, "vs", right)
    if type(left) == type(right) == int:
        if left < right:
            return -1
        elif right < left:
            return +1
        else:
            return 0
    elif type(left) == type(right) == list:
        for l,r in zip(left, right):
            order = cmp(l,r)
            if order in [-1,1]:
                return order
        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return +1
        else:
            return 0
    elif type(left) == list and type(right) == int:
        return cmp(left, [right])
    elif type(left) == int and type(right) == list:
        return cmp([left], right)
    else:
        print("unknown arguments to compare")
        assert(False)

# part 1
indices_in_order = []
for idx, block in enumerate(inputs.split("\n\n"),start=1):
    print(block)
    block = list(map(parse, block.splitlines()))
    order = cmp(block[0], block[1])
    if order == -1:
        print("inputs are in the right order")
        indices_in_order.append(idx)
    elif order == +1:
        print("inputs are NOT in the right order")
    else:
        print("order could not be determined")
    print("--")
print(indices_in_order)
print(sum(indices_in_order))


# part 2
packages = [parse(line) for line in inputs.splitlines() if line != ""] + [[[2]]] + [[[6]]]
decoder_key = math.prod(list(map(itemgetter(0), (filter(lambda x:x[1] in [[[2]], [[6]]], enumerate(sorted(packages, key=functools.cmp_to_key(cmp)), start=1))))))
print(decoder_key)