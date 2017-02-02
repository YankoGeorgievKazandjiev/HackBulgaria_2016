# Task: Is two words anagrams?
def is_anagram(word_one, word_two):
    sorted_word_one = sorted(word_one.lower())
    sorted_word_two = sorted(word_two.lower())
    if sorted_word_one == sorted_word_two:
        return True
    return False
