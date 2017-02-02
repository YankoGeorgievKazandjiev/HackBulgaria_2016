import collections

def prime_number(number):
    is_prime = True
    for smaller_numbers in range(2, number - 1):
        if number % smaller_numbers == 0:
            is_prime = False
    return is_prime

def goldbach(n):
    out_list = []
    dictionary = {}

    for index in range(2, n, 1):
        is_prime = prime_number(index)
        if is_prime:
            next_member = n - index
            next_is_prime = prime_number(next_member)
            if next_is_prime:
                tupl = (index, next_member)
                dictionary[index] = tupl

    sort_list = collections.OrderedDict(sorted(dictionary.items()))

    for index in sort_list:
        if sort_list[index][0] <= sort_list[index][1]:
            out_list.append(sort_list[index])

    return out_list
