import math


#Task 1: Sum of all digits of a number
def sum_of_digits(number):
    result = 0
    if number < 0:
        number = -number
    while number:
        result = result + number % 10
        number = number // 10
    return result


#Task 2: Turn a number into a list of digits
def to_digits(number):
    string_of_numbers = str(number)
    list = []

    for digit in string_of_numbers:
        list.append(int(digit))

    return list


#Task 3:Turn a list of digits into a number
def to_number(n):
    result = 0
    ade = 0
    for digit in n:
        result = result + digit
        result = result * 10
    ade = int(result / 10)
    return ade


#Task 4:Vowels in a string
def count_vowels(str):
    count = 0
    to_lower = str.lower()
    vowels = ["a", "y", "i", "e", "o", "u"]
    for index in to_lower:
        if index in vowels:
            count += 1
    return count


#Task 5:Consonants in a string
def count_consonants(str):
    count = 0
    to_lower = str.lower()
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    for index in to_lower:
        if index in consonants:
            count += 1
    return count


#Task 6:Prime Number
def prime_number(n):
    is_prime = True
    for smaller_numbers in range(2, n - 1):
        if n % smaller_numbers == 0:
            is_prime = False
    return is_prime


#Task 7:Factorial Digits
def fact_digits(number):
    split_number = 0
    result = 0
    while number:
        split_number = number % 10
        number = number // 10
        result += math.factorial(split_number)
    return result


#Task 8:First nth members of Fibonacci
def fibonacci(number):
    listof_fibonacci_numbers = [1]
    if number != 1:
        listof_fibonacci_numbers.append(1)
    for index in range(2, number):
        listof_fibonacci_numbers.append(listof_fibonacci_numbers[index-1]+listof_fibonacci_numbers[index-2])
    return listof_fibonacci_numbers


#Task 9:Fibonacci number
def fib_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_number(n-1) + fib_number(n-2)


#Task 10:Palindrome
def palindrome(obj):
    string = str(obj)
    for symbol in range(len(string) // 2):
        if string[symbol] != string[(len(string) - 1) - symbol]:
            return False
    return True


#Task 11:Char Histogram
def char_histogram(string):
    hash_map = {}
    for index in string:
        hash_map[index] = string.count(index)
    return hash_map
