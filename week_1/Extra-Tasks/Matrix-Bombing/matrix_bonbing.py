
from pprint import pprint

# getting sum of matrix
def get_sum(m):
    return sum(sum(row) for row in m)

# getting neighbours of matrix
def neighbour(matrix):
    neighbours = {}

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            neighbours[(row, col)] = val_neighbours(matrix, row, col)

    return neighbours

# validate neighbours of matrix
def val_neighbours(matrix, row, col):
    neighbours = []

    # validate top neighbours
    if row-1 >= 0:
        for top in range(col-1, col+2):
            if top >= 0 and top < len(matrix[row-1]):
                neighbours.append((row-1, top))
    # validate left neighbours
    if col-1 >= 0:
        neighbours.append((row, col-1))
    # validate right neighbours
    if col+1 < len(matrix[row]):
        neighbours.append((row, col+1))
    # validate bot neighbours
    if row+1 < len(matrix):
        for bot in range(col-1, col+2):
            if bot >=0 and bot < len(matrix[row+1]):
                neighbours.append((row+1, bot))

    return neighbours

def matrix_bombing_plan(m):
    matrix_sum = get_sum(m)
    neigh = neighbour(m)
    new_sum = {}

    for row in range(len(m)):
        for col in range(len(m[row])):
            damage = bombing_matrix(m, row, col, neigh)
            new_sum[(row, col)] = matrix_sum - damage

    return new_sum


def bombing_matrix(matrix, row, col, neighbours):
    #value we are bombing with
    value = matrix[row][col]
    damage_done = 0

    for firs_cordinate, second_cordinate in neighbours[(row, col)]:
        neighbour_value = matrix[firs_cordinate][second_cordinate]
        difference = neighbour_value - value
        if difference >= 0:
            damage_done += value
        else:
            damage_done += neighbour_value

    return damage_done

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result = matrix_bombing_plan(matrix)
    pprint(result)

if __name__ == '__main__':
    main()
