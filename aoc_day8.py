# aoc day 8 - treetop tree house

inputs = """30373
25512
65332
33549
35390""".splitlines()


def parse_map(inputs):    
    tree_map = {}
    for row, line in enumerate(inputs):
        for col, height in enumerate(line.strip()):
            tree_map[(row,col)] = int(height)
    return tree_map, row+1, col+1


def is_visible(tree_map, row, col, n_rows, n_cols):
    return all([tree_map[(r,col)] < tree_map[(row,col)] for r in range(0, row)]) or \
        all([tree_map[(r,col)] < tree_map[(row,col)] for r in range(row+1, n_rows)]) or \
        all([tree_map[(row,c)] < tree_map[(row,col)] for c in range(0, col)]) or \
        all([tree_map[(row,c)] < tree_map[(row,col)] for c in range(col+1, n_cols)])

def scenic_score(tree_map, row, col, n_rows, n_cols):
    look_up = 0
    for r in range(row-1, -1, -1):
        look_up += 1
        if tree_map[(r, col)] >= tree_map[(row, col)]:
            break
    look_down = 0
    for r in range(row+1, n_rows):
        look_down += 1
        if tree_map[(r, col)] >= tree_map[(row, col)]:
            break
    look_left = 0
    for c in range(col-1, -1, -1):
        look_left += 1
        if tree_map[(row, c)] >= tree_map[(row, col)]:
            break
    look_right = 0
    for c in range(col+1, n_cols):
        look_right += 1
        if tree_map[(row, c)] >= tree_map[(row, col)]:
            break
    return look_up*look_down*look_left*look_right

        
tmap, n_rows, n_cols = parse_map(inputs)

# part 1
print(sum([is_visible(tmap, r, c, n_rows, n_cols) for r in range(0, n_rows) for c in range(0, n_cols)]))

# part 2
print(max((scenic_score(tmap, r, c, n_rows, n_cols) for r in range(0, n_rows) for c in range(0, n_cols))))