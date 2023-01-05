# Advent of code day 11: monkey in the middle

from collections import defaultdict
from operator import itemgetter
import math

inputs = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

def parse_input(inputs):
    monkeys = []
    for block in inputs.split("\n\n"):
        _, items, operation, modulo, if_true, if_false =  block.splitlines()
        items = list(map(int, items[17:].split(",")))
        operation = operation[19:]
        modulo = int(modulo.split()[-1])
        next_monkey_if_true = int(if_true.split()[-1])
        next_monkey_if_false = int(if_false.split()[-1])
        monkeys.append((items, operation, modulo, next_monkey_if_true, next_monkey_if_false))
    return monkeys

def next_turn(monkey, divide=True, modulo=None):
    items, operation, modulo_test, next_monkey_if_true, next_monkey_if_false = monkey
    throw = defaultdict(list)
    for i in range(len(items)):
        old = items.pop(0)
        new = eval(operation)
        if modulo:
            new = new % modulo
        if divide:
            new = new//3
        next_monkey = next_monkey_if_true if new % modulo_test == 0 else next_monkey_if_false
        throw[next_monkey].append(new)
    return throw

def print_status(monkeys):
    for i in range(len(monkeys)):
        print("Monkey %d: %s" % (i, ",".join(map(str, monkeys[i][0]))))

def round(monkeys, inspection_count, divide=True, modulo=None):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        inspection_count[i] += len(monkey[0])
        throw = next_turn(monkey, divide, modulo)
        for monkey, items in throw.items():
            monkeys[monkey][0].extend(items)

def compute_monkey_business(inspection_count):
    # find two most active monkeys# find two most active monkeys    
    return math.prod(sorted(inspection_count.values(), reverse=True)[:2])
    
# part 1
monkeys = parse_input(inputs)
inspection_count = {m:0 for m in range(len(monkeys))}
for r in range(20):
    round(monkeys, inspection_count)
    print("After round ", r+1)
    print_status(monkeys)
print(compute_monkey_business(inspection_count))

# part 2
monkeys = parse_input(inputs)
inspection_count = {m:0 for m in range(len(monkeys))}
modulo = math.prod(map(itemgetter(2), monkeys))
for r in range(10000):
    round(monkeys, inspection_count, divide=False, modulo=modulo)
    if r ==0 or r == 19 or (r+1)%1000 == 0:
        print("== After round ", r+1, "==")
        for key, value in inspection_count.items():
            print("Monkey %d inspected items %d times." % (key, value))
print(compute_monkey_business(inspection_count))            


