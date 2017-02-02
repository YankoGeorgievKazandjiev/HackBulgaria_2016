#Task 1:Counting substrings
def count_substrings(haystack, needle):
    result = 0
    for index in haystack:
        result = haystack.count(needle)
    return result


# Task 2:Sum Numbers in Matrix
def sum_matrix(m):
    result = 0
    for index in m:
        result = result+sum(index)
    return result


#  Task 3:NaN Expand
def nan_expand(times):
    string = "Not a "
    result = ""
    b = "NaN"
    while times > 0:
        result = string*times + b
        times = times-1
        return result
    return result


#   Task 4:Integer prime factorization
def prime_factorization(n):
    list_of_numbers = [2, 3, 5, 7, int(n)]
    result = []
    for prime in list_of_numbers:
        count = 0
        while n > 0:
            while n % prime == 0:
                n = n / prime
                count+=1
            else:
                break
        if count > 0:
            result.append((prime, count))
    if n > 1:
        result.append((int(n), 1))
    return result


#   Task 5:The group function
def group(items):
    if len(items) == 0:
        return []

    grouped_items = []
    prev_item, rest_items = items[0], items[1:]

    subgroup = [prev_item]
    for item in rest_items:
        if item != prev_item:
            grouped_items.append(subgroup)
            subgroup = []
        subgroup.append(item)
        prev_item = item

    grouped_items.append(subgroup)
    return grouped_items


#   Task 6:Longest subsequence of equal consecutive elements
def max_consecutive(list_of_numbers):
    count_temp = 0
    end_result = 0
    for index in range(len(list_of_numbers)-1):
        if list_of_numbers[index] == list_of_numbers[index+1]:
            count_temp += 1
        else:
            if count_temp > end_result:
                end_result = count_temp
            count_temp = 1
    if count_temp > end_result:
        return count_temp
    else:
        return end_result


#Task 7:Word counter
def word_counter(word):
    search_word = word
    matrix_sizes = input().split(" ")
    n_rows = int(matrix_sizes[0])
    n_cols = int(matrix_sizes[1])

    if len(search_word) > n_rows:
        return "Invalid number of rows or columns!"

    matrix = [[] for x in range(n_rows)]
    for row in range(n_rows):
        matrix[row] += filter(lambda x: x != ' ', input())

    all_hyperrows = []

# diagonals
    for offset in range(abs(n_rows - n_cols) + 1):
        go_right = (n_cols > n_rows) * offset
        go_down = (n_rows > n_cols) * offset
        d1, d2 = list(), list()
        for x in range(min(n_rows, n_cols)):
            d1 += matrix[x + go_down][x + go_right]
            d2 += matrix[x + go_down][n_cols - go_right - x - 1]
        all_hyperrows.append(d1)
        all_hyperrows.append(d2)

# horizontal lines
    all_hyperrows.extend(matrix)

# vertical lines
    for col_idx in range(n_cols):
        vertical_row = list()
        for row_idx in range(n_rows):
            vertical_row += matrix[row_idx][col_idx]
        all_hyperrows.append(vertical_row)

    all_strs = [''.join(all_hyperrows[x]) for x in range(len(all_hyperrows))]

    count_words = sum([count_substrings(strn, search_word) for strn in all_strs if strn])
    count_words += sum([count_substrings(strn, search_word[::-1]) for strn in all_strs if strn])

    if palindrome(search_word):
        count_words = int(count_words / 2)
    return count_words
