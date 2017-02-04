ALL_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sudoku_solved(sudoku):
    if sudoku_rows(sudoku) and sudoku_colms(sudoku) and sudoku_squares(sudoku) is True:
        return True
    return False

def sudoku_rows(sudoku):
    # sort row by row and check numbers from ALL_NUMBERS
    for row in sudoku:
        if sorted(row) != ALL_NUMBERS:
            return False
    return True

def sudoku_colms(sudoku):
    # write column by column in list_of_colums then sort them and chek numbers in ALL_NUMBERS
    for col in range(len(sudoku)):
        list_of_colums =[None]*9
        for row in range(len(sudoku)):
            list_of_colums[row] = sudoku[row][col]
        if sorted(list_of_colums) != ALL_NUMBERS:
            return False
    return True

def sudoku_squares(sudoku):
    # Take squares by 3x3 write them in list, then sort them and chek numbers in ALL_NUMBERSs
    for hor_sqr in range(3):
        for ver_sqr in range(3):
            new_sqr = []
            for row in range(3):
                for col in range(3):
                    new_sqr.append(sudoku[(hor_sqr * 3)+row][(ver_sqr * 3)+col])
            if sorted(new_sqr) != ALL_NUMBERS:
                return False
    return True

print(sudoku_squares([
[4, 5, 2, 3, 8, 9, 7, 1, 6],
[3, 8, 7, 4, 6, 1, 2, 9, 5],
[6, 1, 9, 2, 5, 7, 3, 4 ,8],
[9, 3, 5, 1, 2, 6, 8, 7, 4],
[7, 6, 4, 9, 3, 8, 5, 2, 1],
[1, 2, 8, 5, 7, 4, 6, 3, 9],
[5, 7, 1, 8, 9, 2, 4, 6, 3],
[8, 9, 6, 7, 4, 3, 1, 5 ,2],
[2, 4, 3, 6, 1, 5, 9, 8, 7]
]))

# print(sudoku_solved([
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]))
