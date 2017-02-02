Final Round

In a file, called finalround.py, code the solutions to the following problems:

The solutions should be written in Python 3.

1.Is Number Balanced?

A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number 1238033 is balanced, because it's left part is 123 and right part is 033.

We have : 1 + 2 + 3 = 0 + 3 + 3 = 6.

A number with only one digit is always balanced!

Implement a function is_number_balanced(n) that checks if n is balanced.

Test Examples

>>> is_number_balanced(9)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True
2.Increasing and Decreasing Sequences

Implement the following function:

2.1 Increasing sequnce?

Implement a function, called increasing_or_decreasing(seq) where seq is a list of integers.

The function should return Up!, if the given sequence is monotonously increasing. If monotonously decreasing return Down! . If both of the condintions are not satisfied, then return False.

And before you skip this problem, because of the math terminology, let me explain:

A sequence is monotonously increasing if for every two elements a and b, that are next to each other (a is before b), we have a < b.

For example, [1,2,3,4,5] is monotonously increasing, but [1,2,3,4,5,1] is not.

Test Examples

>>> increasing_or_decreasing([1,2,3,4,5])
Up!
>>> increasing_or_decreasing([5,6,-10])
False
>>> increasing_or_decreasing([1,1,1,1])
False
>>> increasing_or_decreasing([9,8,7,6])
Down!
3. Largest Palindrome

Implement a function get_largest_palindrome(n), which return the largest palindrome smaller than n. Given number n can also be palindrome.

Test Examples

>>> get_largest_palindrome(99)
88
>>> get_largest_palindrome(252)
242
>>> get_largest_palindrome(994687)
994499
>>> get_largest_palindrome(754649)
754457
4. Sum all numbers in a given string

You are given a string, where there can be numbers. Return the sum of all numbers in that string (not digits, numbers)

Examples:

sum_of_numbers("1111") = 1111
sum_of_numbers("1abc33xyz22") = 1 + 33 + 22 = 56
sum_of_numbers("abcd") = 0
Signature

def sum_of_numbers(st):
    pass
Test Examples

>>> sum_of_numbers("ab125cd3")
128
>>> sum_of_numbers("ab12")
12
>>> sum_of_numbers("ab")
0
5. Birthday Ranges

Implement a function birthday_ranges(birthdays, ranges) We have a list birthdays and list of tuples ranges. birthdays - range from 0 to 365, ranges - ranges (one range is a tuple of two numbers - start and end0.

We want to calculate, for each tuple, how many people are born in that range (between start and end inclusive).

For example:

Birthdays - [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15]
Ranges - [(4, 9), (6, 7), (200, 225), (300, 365)]
Will give the result:

[5, 2, 0, 1]
As we can see, betweeh 4 and 9, inclusive, there are 5 people with birthdays - 5, 6, 7, 4, 5.Between 300 and 365 there is exatly one birthday - 300.

Test Examples

>>> birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])
[2, 3, 4, 5, 2]
6. 100 SMS

Before the smartphones, when you had to write some message, the keypads looked like that:

Nokia 3310 Keypad

For example, on such keypad, if you want to write Ruby, you had to press the following sequence of numbers:

7778822999
Each key contains some letters from the alphabet. And by pressing that key, you rotate the letters until you get to your desired one.

It's time to implement some encode / decode functions for the old keypads!

numbers_to_message(pressed_sequence)

First, implement the function that takes a list of integers - the sequence of numbers that have been pressed. The function should return the corresponding string of the message.

There are a few special rules:

If you press 1, the next letter is going to be capitalized
If you press 0, this will insert a single white-space
If you press a number and wait for a few seconds, the special breaking number -1 enters the sequence. This is the way to write different letters from only one keypad!
Few examples:

numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]) = "abc"
numbers_to_message([2, 2, 2, 2]) = "a"
numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])
=
"Ivo e Panda"
message_to_numbers(messsage)

This function takes a string - the message and returns the minimal keystrokes that you need to write that message

Few examples:

message_to_numbers("abc") = [2, -1, 2, 2, -1, 2, 2, 2]
message_to_numbers("a") = [2]
message_to_numbers("Ivo e Panda")
=
[1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
message_to_numbers("aabbcc") = [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
