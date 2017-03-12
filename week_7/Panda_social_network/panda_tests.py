import unittest
from panda_social_network import PandaSocialNetwork
from Exceptions import *
from Panda import Panda

class SocialNetworkTests(unittest.TestCase):
    def setUp(self):
        self.ivo = Panda('Ivo', 'ivo@gmail.com', 'male')
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.same_rado = Panda("Rado", "rado@pandamail.com", "male")
        self.tony = Panda("Tony", "tony@pandamail.com", "female")

        self.social_network = PandaSocialNetwork()

    def test_add_panda(self):
        social_network = PandaSocialNetwork()
        social_network.add_panda(self.rado)
        social_network.add_panda(self.tony)
        self.assertEqual(social_network.pandas, [self.rado, self.tony])

    def test_has_panda(self):
        social_network = PandaSocialNetwork()
        social_network.add_panda(self.rado)
        self.assertTrue(social_network.has_panda(self.rado))

    def test_make_friends(self):
        social_network = PandaSocialNetwork()

        social_network.make_friends(self.ivo, self.tony)
        with self.assertRaises(PandasAlreadyFriends):
            social_network.make_friends(self.ivo, self.rado)

    def test_are_friends(self):
        social_network = PandaSocialNetwork()
        social_network.make_friends(self.ivo, self.rado)
        social_network.make_friends(self.ivo, self.tony)
        self.assertTrue(social_network.are_friends(self.ivo, self.rado))
        self.assertTrue(social_network.are_friends(self.ivo, self.tony))
        self.assertFalse(social_network.are_friends(self.rado, self.tony))

    def test_save_load(self):
        file_name = 'saved.json'
        self.social_network.save(file_name)
        loaded_social_network = PandaSocialNetwork.load(file_name)

        self.assertEqual(loaded_social_network.how_many_gender_in_network(1, self.friendless_guy, 'male'), 0)
        self.assertEqual(loaded_social_network.how_many_gender_in_network(1, self.girl, 'female'), 0)


if __name__ == '__main__':
    unittest.main()
