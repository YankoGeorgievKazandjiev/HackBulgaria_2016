def is_credit_card_valid(number):
    convert_to_str_reverst = str(number)[::-1]
    number_after_chek = ''

    if len(convert_to_str_reverst) % 2 == 0:
        return "Invalid number!"
    #Indexing number and multipl it
    for index, digit in enumerate(convert_to_str_reverst):
        if index % 2 != 0:
            number_after_chek += str(2 * int(digit))
        else:
            number_after_chek += digit
    # sum digits
    result = sum(int(digit) for digit in number_after_chek)
    if result % 10 == 0:
        return True
    else:
        return False
