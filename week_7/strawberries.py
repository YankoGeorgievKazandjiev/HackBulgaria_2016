NEIGHBOURS = [(0, -1), (0, 1), (1, 0), (-1, 0)]
CORDINATES_OF_DEAD_STRAW = set()

def strawberries(rows, columns, days, dead_strawberries):
    global CORDINATES_OF_DEAD_STRAW
    CORDINATES_OF_DEAD_STRAW = set()

    if 0 > rows or rows > 10000 or 0 > columns or columns > 10000 or days < 0 or days > 1000:
        raise ValueError()

    matrix = [[True] * columns for index in range(rows)]

    for row, col in dead_strawberries:
        matrix[row][col] = False

    for index in range(days):
        dead_strawberries = pass_days(matrix, dead_strawberries)

    alive_strawberries = sum([sum(row) for row in matrix])
    return alive_strawberries


def pass_days(matrix, dead_strawberries):
    next_dead_strawb = []
    for row, col in dead_strawberries:
        if (row, col) not in CORDINATES_OF_DEAD_STRAW:
            for row_in_cord, col_in_cord in NEIGHBOURS:
                new_row = row + row_in_cord
                new_col = col + col_in_cord
                if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[new_row]):
                    matrix[new_row][new_col] =  False
                    next_dead_strawb.append((new_row, new_col))
        CORDINATES_OF_DEAD_STRAW.add((row, col))
    return next_dead_strawb


def main():
    print(strawberries(8, 10, 2, [(4, 8), (2, 7)]))

if __name__ == "__main__":
    main()
