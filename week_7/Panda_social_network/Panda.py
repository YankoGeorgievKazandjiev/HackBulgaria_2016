import re
from Exceptions import InvalidEmailError

VALID_EMAIL = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class Panda:
    def __init__(self, name, email, gender):
        if not re.search(VALID_EMAIL, email):
            raise InvalidEmailError('Invalid email!!!')
        self.name = name
        self.email = email
        self.gender = gender

    def __str__(self):
        return 'Panda - {}'.format(self.name)

    def __eq__(self, other):
        return(self.email.lower() == other.email.lower()) and\
              (self.name.lower() == other.name.lower()) and\
              (self.gender.lower() == other.gender.lower())

    def __hash__(self):
        return hash(self.name + self.email + self.gender)

    def gender(self):
        return self.gender

    def name(self):
        return self.name

    def email(self):
        return self.email

    def isMale(self):
        return self.gender.lower() == 'male'

    def isFemale(self):
        return self.gender.lower() == 'female'
