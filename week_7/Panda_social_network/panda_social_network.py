from Panda import Panda
from Exceptions import PandasAlreadyFriends


class PandaSocialNetwork:
    def __init__(self):
        self.pandas = []
        self.relationships = {}

    def add_panda(self, panda: Panda):
        if panda.name in self.pandas:
            raise PandaAlreadyThereError()

        self.pandas.append(panda.name)
        self.relationships[panda] = []

    def has_panda(self, panda: Panda):
        return panda in self.pandas

    def make_friends(self, panda1, panda2):
        if panda1.name not in self.pandas:
            self.add_panda(panda1)
        if panda2.name not in self.pandas:
            self.add_panda(panda2)

        self.relationships[panda1].append(panda2)
        self.relationships[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda1 in self.relationships[panda2]

    def friends_of(self, panda: Panda):
        if panda not in self.relationships.keys():
            return False
        return self.relationships[panda]

    def connection_level(self, panda1, panda2):
        pass
        # TO BE DON

    def are_connected(self, panda1, panda2):
        pass
        # TO BE DON
    def how_many_gender_in_network(self, searched_level, panda, gender):
        pass
        # TO BE DON

    def save(self, file_name):
        pandas = [str(panda.__dict__) for panda in self.pandas]
        relationships = {str(panda.__dict__): [str(panda_index.__dict__) for panda_index in friends] for panda, friends in self.relationships.items()}

        dara = {'pandas': pandas, 'relationships': relationships}
        with open(file_name, "w", encoding = 'utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def load(file_name):
        pass
        # TO BE DON
