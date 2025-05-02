from constraint import Problem

rectangles = {"R1": (6, 4), "R2": (5, 2), "R3": (2, 2),
              "R4": (3, 2), "R5": (1, 8), "R6": (1, 4)}
board = (7, 8)


def no_overlap(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 + w1 <= x2 or x2 + w2 <= x1 or y1 + h1 <= y2 or y2 + h2 <= y1  # check if rectangle ends before new one


def solve():
    problem = Problem()
    positions = {}

    for name, (width, height) in rectangles.items():
        pos_list = []

        # Horizontal orientation
        for x in range(board[0] - width + 1):
            for y in range(board[1] - height + 1):
                pos_list.append((x, y, width, height, 0))  # 0 = horizontal

        # Vertical orientation
        if width != height:  # Only add vertical if different from horizontal
            for x in range(board[0] - height + 1):
                for y in range(board[1] - width + 1):  # max x-position at which it fits in the container
                    pos_list.append((x, y, height, width, 1))  # 1 = vertical

        positions[name] = pos_list
        problem.addVariable(name, pos_list)

    # Add no-overlap constraints
    keys = list(positions.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):  # iterate through all pairs
            problem.addConstraint(
                lambda pos1, pos2: no_overlap(pos1[0], pos1[1], pos1[2], pos1[3],  # tuples (x, y, height, width, 1)
                                              pos2[0], pos2[1], pos2[2], pos2[3]),
                (keys[i], keys[j])
            )

    return problem.getSolutions()


solutions = solve()

if not solutions:
    print("No solutions found.")
else:
    print(f"Found {len(solutions)} solutions. Showing first solution:\n")
    solution = solutions[0]

    for name, (width, height) in rectangles.items():
        pos = solution[name]
        x, y, actual_width, actual_height, rot = pos
        print(f"{name}: Position ({x},{y}), Size ({actual_width}x{actual_height}), "
              f"Orientation: {'horizontal' if rot == 0 else 'vertical'}")
