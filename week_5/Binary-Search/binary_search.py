def binary_search(array, start, end, element):
    mid_index = (start + end)//2
    if array[mid_index] == element:
        return mid_index
    if array[mid_index] > element:
        return binary_search(array, start, mid_index-1, element)
    elif array[mid_index] < element:
        return binary_search(array, mid_index+1, end, element)

def find_turning_point(array, start, end):
    mid_index = (start + end) // 2
    if array[mid_index - 1] < array[mid_index] and array[mid_index] > array[mid_index + 1]:
        return "Turning point is {0} on index {1}.".format(array[mid_index+1], mid_index+1)
    elif array[mid_index-1] < array[mid_index] and array[mid_index] < array[mid_index+1]:
        return find_turning_point(array, mid_index, end)
    elif array[mid_index-1] > array[mid_index] and array[mid_index] > array[mid_index+1]:
        return find_turning_point(array, start, mid_index)
