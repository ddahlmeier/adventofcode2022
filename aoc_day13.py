# Advent of Code 13: Distress Signal

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

def in_order(left, right):
    print("Compare", left, "vs", right)
    if type(left) == type(right) == int:
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return None
    elif type(left) == type(right) == list:
        for l,r in zip(left, right):
            order = in_order(l,r)
            if order == True or order == False:
                return order
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False
        else:
            return None
    elif type(left) == list and type(right) == int:
        return in_order(left, [right])
    elif type(left) == int and type(right) == list:
        return in_order([left], right)
    else:
        print("unknown arguments to compare")
        assert(False)

# part 1
indices_in_order = []
for idx, block in enumerate(inputs.split("\n\n"),start=1):
    print(block)
    block = list(map(parse, block.splitlines()))
    order = in_order(block[0], block[1])
    if order == True:
        print("inputs are in the right order")
        indices_in_order.append(idx)
    elif order == False:
        print("inputs are NOT in the right order")
    else:
        print("order could not be determined")
    print("--")
print(indices_in_order)
print(sum(indices_in_order))


