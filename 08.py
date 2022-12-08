def check_visible_side(trees, is_top, start, delta) -> set:
    visible = set()
    if not is_top:
        side_length = len(trees)
        end = len(trees[0])
    else:
        side_length = len(trees[0])
        end = len(trees)

    for i in range(side_length):
        cur_height = -1
        j = start
        while (delta > 0 and j < end) or (delta < 0 and j >= 0):
            if is_top and trees[j][i] > cur_height:
                cur_height = trees[j][i]
                visible.add((j, i))
            elif not is_top and trees[i][j] > cur_height:
                cur_height = trees[i][j]
                visible.add((i, j))
            j += delta

    return visible

def visible_trees_direction(trees, i, j, delta_i, delta_j) -> int:
    house_heigth = trees[i][j]
    count = 0
    i += delta_i
    j += delta_j
    while i >= 0 and i < len(trees) and j >= 0 and j < len(trees[0]):
        if trees[i][j] < house_heigth:
            count += 1
        elif trees[i][j] >= house_heigth:
            count += 1
            break
        i += delta_i
        j += delta_j
    
    return count

def get_scenic_score(trees, i, j) -> int:
    score = visible_trees_direction(trees, i, j, 1, 0)
    score *= visible_trees_direction(trees, i, j, -1, 0)
    score *= visible_trees_direction(trees, i, j, 0, 1)
    score *= visible_trees_direction(trees, i, j, 0, -1)
    return score

f = open("08_input.txt")
lines = f.readlines()
trees = []
for line in lines:
    trees.append([int(c) for c in line.strip()])

height = len(trees)
width = len(trees[0])

visible = check_visible_side(trees, False, 0, 1)
visible = visible.union(check_visible_side(trees, False, width - 1, -1))
visible = visible.union(check_visible_side(trees, True, 0, 1))
visible = visible.union(check_visible_side(trees, True, height - 1, -1))

visible_trees = len(visible)

print("08_a: " + str(visible_trees))

max_scenic_score = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        score = get_scenic_score(trees, i, j)
        if score > max_scenic_score:
            max_scenic_score = score

get_scenic_score(trees, 3, 2)
print("08_b: " + str(max_scenic_score))