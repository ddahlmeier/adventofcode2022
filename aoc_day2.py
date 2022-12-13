inputs = """A Y
B X
C Z"""

strategy = list(map(lambda x:tuple(x.split()), inputs.splitlines()))

## part 1
#               Player 1        Player 2
# Rock:             A               X
# Paper:            B               Y
# Scissors:         C               Z

# Value of shape selected
# Rock: 1 point
# Paper: 2 points
# Scissors: 3 points

# Win: 6 points
# Draw: 3 points
# Lose: 0 points


outcome = dict([(('A', 'X'), 3),
 (('A', 'Y'), 6),
 (('A', 'Z'), 0),
 (('B', 'X'), 0),
 (('B', 'Y'), 3),
 (('B', 'Z'), 6),
 (('C', 'X'), 6),
 (('C', 'Y'), 0),
 (('C', 'Z'), 3)])

shape_value = {"X":1, "Y":2, "Z":3}

score_part1 = sum(outcome[round]+shape_value[round[1]] for round in strategy)

## part 2
# X: you need to lose
# Y: you need to draw
# Z: you need to win

response = dict([(('A', 'X'), 'C'),
 (('A', 'Y'), 'A'),
 (('A', 'Z'), 'B'),
 (('B', 'X'), 'A'),
 (('B', 'Y'), 'B'),
 (('B', 'Z'), 'C'),
 (('C', 'X'), 'B'),
 (('C', 'Y'), 'C'),
 (('C', 'Z'), 'A')])


outcome_part2 = dict([(('A', 'A'), 3),
 (('A', 'B'), 6),
 (('A', 'C'), 0),
 (('B', 'A'), 0),
 (('B', 'B'), 3),
 (('B', 'C'), 6),
 (('C', 'A'), 6),
 (('C', 'B'), 0),
 (('C', 'C'), 3)])

shape_value2 = {"A":1, "B":2, "C":3}

score_part2 = sum([outcome_part2[(player1, response[(player1, end)])] + shape_value2[response[(player1,end)]] for player1, end in strategy])
