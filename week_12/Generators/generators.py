def chain(iterable_one, iterable_two):
    for iter_1 in iterable_one:
        yield iter_1
    for iter_2 in iterable_two:
        yield iter_2

# print(list(chain(range(0, 4), range(4, 8))))

def compress(iterable, mask):
    for index in range(len(mask)):
        if mask[index] is True:
            yield iterable[index]

# print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))

def cycle(iterable):
    while True:
        for index in iterable:
            yield index

# endless = cycle(range(0,10))
# for item in endless:
#     print(item)
