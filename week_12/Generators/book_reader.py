import os

def read_book():
    book_count = 1
    while True:
        book_name = str(book_count).zfill(3) + '.txt'

        if not os.path.isfile(book_name):
            break

        chapter = []
        with open(book_name) as f:

            lines = f.readlines()
            for line in lines:
                if line.startswith('# Chapter'):
                    yield ''.join(chapter)
                chapter.append(line)
        yield ''.join(chapter)
        book_count +=1

for i in read_book():
    command = input()
    while command != ' ':
        command = input()
