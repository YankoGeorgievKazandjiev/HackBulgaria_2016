
import re


# Task 1:Is Number Balanced?
def to_list(number):
    list_of_numbers = []
    while number > 0:
        list_of_numbers.append(number % 10)
        number //= 10
    return list_of_numbers[::-1]


def is_number_balanced(number):
    if number // 10 == 0:
        return True
    list_of_numbers = to_list(number)
    middle_index = len(list_of_numbers) // 2
    if len(list_of_numbers) % 2 == 0:
        if(sum(list_of_numbers[middle_index::]) ==
                sum(list_of_numbers[:middle_index:])):
                return True
    elif (sum(list_of_numbers[middle_index + 1::]) ==
            sum(list_of_numbers[:middle_index:])):
            return True
    return False


# Task 2:Increasing and Decreasing Sequences
def increasing_or_decreasing(seq):
    diff = [seq[index + 1] - seq[index] for index in range(len(seq) - 1)]
    if len(set(diff)) == 1:
        if diff[0] > 0:
            return "Up!"
        if diff[0] < 0:
            return "Down!"
    return False


# Task 3:Largest Palindrome
def palindrome(obj):
    string = str(obj)
    is_polindrom = (string == string[::-1])
    return is_polindrom


def get_largest_palindrome(number):
    result = []
    for num in range(number):
        if palindrome(num):
            result.append(num)
    return result[-1]


# Task 4:Sum all numbers in a given string
def sum_of_numbers(st):
    result = sum([int(number.group()) for number in re.finditer('\d+', st)])
    return result


# Task 5:Birthday Ranges
def birthday_ranges(birthdays, ranges):
    result = []
    for start, end in ranges:
        result.append([birthday for birthday in birthdays
                       if start <= birthday <= end])
    result = [len(birthday) for birthday in result]
    return result
 

# Task 6:100 SMS
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

CAPITAL_KEY = 1
BREAK_KEY = -1
SPACE_KEY = 0

key_combinatios = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}

def numbers_to_message(pressed_sequence):
    groups = group(pressed_sequence)
    print(groups)
    sms = ''
    capital = False
    for index in groups:
        if index[0] == SPACE_KEY:
            sms += ' '
        elif index[0] == CAPITAL_KEY:
            capital = True
        elif index[0] == BREAK_KEY:
            continue
        else:
            sequence_key = index[0]

            key_length = len(key_combinatios[sequence_key])
            count = len(index) % key_length

            if count == 0:
                count = key_length

            index = [sequence_key] * count
            word = key_combinatios[sequence_key][len(index)-1]

            if capital:
                word = word.upper()
                capital = False

            sms +=word

    return sms

reverst_dict = {letter: str(k)*(idx+1) for k, v in key_combinatios.items()
                               for idx, letter in enumerate(v)}

def message_to_numbers(massage):
    result = []
    for index in massage:
        if index.isupper():
            result.append(1)
        if index == ' ':
            result.append(0)
        else:
            lower = reverst_dict[index.lower()]
            seq_list = list(lower)

            seq_list = [int(digit) for digit in seq_list]

            if result and result[-1] == seq_list[0]:
                result.append(-1)
            result.extend(seq_list)
    return result
