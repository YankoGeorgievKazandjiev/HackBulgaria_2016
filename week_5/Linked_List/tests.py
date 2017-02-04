import unittest
from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_adding_element(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.size(), 1)
    
    def test_remove_element(self):
        self.ll.add_element(4)
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)
    
    def test_add_first_element(self):
        self.ll.add_first(30) #check first el
        self.assertEqual(self.ll.head.value, 30)
        self.ll.add_first(12) #check tail el after add second el
        self.assertEqual(self.ll.tail.value, 30)
    
    def test_get_index_of_element(self):
        node = self.ll.get_index(0)#test empty list
        self.assertEqual(node, None)
    
        self.ll.add_element(1) #test index with elements
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.assertEqual(self.ll.get_index(1).value, 2)
    
    def test_to_list_func(self):
        self.ll.add_element(1)
        self.ll.add_element(4)
        self.ll.add_element(3)
        self.assertEqual(self.ll.to_list(),[1, 4, 3])
    
    def test_add_at_index(self):
        #invalid indexes
        self.assertFalse(self.ll.add_at_index(1,3), False)
        self.assertEqual(self.ll.add_at_index(0,5), None)
    
    def test_ll_from_to(self):
        self.ll.add_list([1,2,3,4,5,6,7])
        new_ll = self.ll.ll_from_to(3,6)
        self.assertEqual(new_ll.head.value, 4)
        self.assertEqual(new_ll.tail.value, 7)
        self.assertEqual(new_ll.to_list(), [4,5,6,7])

    def test_pop_func(self):
        # test tail of the list is it pop one el
        self.ll.add_list([1,2,3])
        self.ll.pop()
        self.assertEqual(self.ll.tail.value, 2)
        self.ll.pop()
        self.assertEqual(self.ll.tail.value, 1)

    def test_reduce_to_unique(self):
        orig_list = [0,0,1,0,0,1,2,3,2]
        expected_list = [0,1,2,3]
        self.ll.add_list(orig_list)
        self.assertEqual(self.ll.to_list(), orig_list)
        unique_ll = self.ll.reduce_to_unique()
        self.assertNotEqual(unique_ll.to_list(), orig_list)
        self.assertEqual(unique_ll.to_list(), expected_list)

    def test_add_to_linked_list(self):
        new_ll = LinkedList()
        new_ll.add_element(1)
        new_ll.add_element(2)
        new_ll.add_element(3)
        self.ll.add_element(0)
        self.ll.add_linked_list(new_ll)
        self.assertEqual(self.ll.head.value, 0)
        self.assertEqual(self.ll.tail.value, 3)
        self.assertEqual(self.ll.to_list(), [0,1,2,3])


if __name__ == '__main__':
    unittest.main()
