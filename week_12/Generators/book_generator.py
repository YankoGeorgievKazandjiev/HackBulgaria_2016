import random

def generate_book():
    check_capital = bool(random.randint(0, 1))

    if check_capital:
        return chr(random.randint(65, 90))
    else:
        return chr(random.randint(97, 122))

print("Enter chapter count and lenght:\n")
chapter_count = int(input('>'))
chapter_length = int(input('>'))

book = open('book_generator.txt', 'w')
for index in range(chapter_count):
    book.write("Chapter #{}\n".format(index+1))
    while chapter_length > 0:
        new_line = not bool(random.randint(0, 150))
        word_lenght = random.randint(2, max(2, min(12, chapter_length)))
        chapter_length -= word_lenght + 1
        word = ''.join(generate_book() for index in range(word_lenght))
        book.write(word + ' ')
        if new_line:
            book.write('\n')
    book.write('\n\n')
