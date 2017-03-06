import os
f_path = os.path.abspath("log.txt")
import datetime
import timeit
from time import sleep


def accepts(*arguments):
    def check(func):
        f = func.__code__
        assert len(arguments) == f.co_argcount

        def decorated(*args, **kwargs):
            position = 0
            for (arg, type_of_all) in zip(args, arguments):
                position += 1
                if not isinstance(arg, type_of_all):
                    raise TypeError("Argument {0} of {1} is not {2}").format(position, func.__name__, type_of_all)
            return func(*args, **kwargs)
        return decorated
    return check

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

def encrypt(value):
    def caesar_cipher(func):
        def decorated(*args, **kwargs):
            text = func(*args, **kwargs)
            encrypt_text = encode(text, value)
            return encrypt_text
        return decorated
    return caesar_cipher

def log(txt_file):
    def accepter(func):
        def decorator(*args, **kwargs):
            result_string = func(*args, **kwargs)
            string = "function {} at {}".format(func.__name__, datetime.datetime.now())
            with open(txt_file, 'a') as f:
                f.write(string + "\n")
            return result_string
        return decorator
    return accepter

@log(f_path)
@encrypt(2)
def get_low():
    return "Get get get low"

def encode(text, value):
    cipherText = ""
    for index in text:
        if index.isalpha():
            encode_text = ord(index) + value
            if encode_text > ord('z'):
                encode_text -=26
            result = chr(encode_text)
            cipherText += result
        if index is " ":
            cipherText += " "
    return cipherText

def performance(file_name):
    def _performance(func):
        def func_wrapper(*args, **kwargs):
            start = timeit.default_timer()
            func(*args, **kwargs)
            end = timeit.default_timer()
            with open(file_name, 'a') as f:
                f.write("{func_name} was called and took {elapsed_time:.2f} seconds to complete\n".format(
                    func_name=func.__name__,
                    elapsed_time=end-start
                ))
        return func_wrapper
    return _performance


@performance(f_path)
def sleep_lower():
    sleep(2)
    return "I am done!"


def main():
    # print(say_hello("Yanko"))
    # print(deposit("Yanko", 5))
    # print(get_low())
    sleep_lower()

if __name__ == "__main__":
    main()
