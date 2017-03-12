import hashlib
from user_interface import validators

class User(object):
    def __init__(self):
        self.username = None
        self.password = None

    def hash_pass(func):
        def decorated(self, password):
            hashed = hashlib.sha1(password.encode('utf-8')).hexdigest()
            return func(self, password)
        return decorated

    def validated_pass(func):
        def decorated(self, password):
            if not validators.validate_pass(password):
                print("Invalis password!!!")
                return False
            return func(self, password)
        return decorated


    @validated_pass
    @hash_pass
    def set_pass(self, password):
        self.password = password
        return True

    def set_username(self, username):
        self.username = username
        return True

    @staticmethod
    def hash_string(password):
        return hashlib.sha1(password.encode('utf-8')).hexdigest()
