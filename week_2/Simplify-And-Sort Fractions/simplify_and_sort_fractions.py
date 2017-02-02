def greatest_common_divisor(first_number, second_number):
    if first_number == second_number:
        return first_number
    if first_number > second_number:
        return greatest_common_divisor(first_number -
                                       second_number, second_number)
    if first_number < second_number:
        return greatest_common_divisor(second_number, first_number)


def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    gcd = greatest_common_divisor(nominator, denominator)
    return (int(nominator / gcd), int(denominator / gcd))

def least_common_multiple(first_number, second_number):
    gcd = greatest_common_divisor(first_number, second_number)
    if gcd == 1:
        return first_number * second_number
    else:
        return (first_number * second_number) / gcd


def get_lcm_of_list(denominators):
    lcm = least_common_multiple(denominators[0], denominators[1])
    for index in range(2, len(denominators)):
        lcm = least_common_multiple(lcm, denominators[index])
    return lcm

def sort_fractions(fractions):
    return sorted(fractions,key=lambda x: x[0] / x[1])
