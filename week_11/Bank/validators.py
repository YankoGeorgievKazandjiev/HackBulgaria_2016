import re
import getpass
import hashlib

#Validate if pass is longer then 8 chars,have capital letter and special chars

def validate_pass(password):
    special_chars = re.compile("[\@\!\#\$\%\^\&\*\(\)\_]")
    capital = re.compile("[A-Z]")

    if len(password) < 8:
        print("To short password!")
        return False

    if not special_chars.search(password):
        print("No special characters!")
        return False

    if not capital.search(password):
        print("No capital letter in pass!")
        return False
    return True

# hash the password with sha256

def hash_pass(password):
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed
