class Node:
    def __init__(self, value, next_n, prev_n, index):
        self.value = value
        self.next = next_n
        self.prev = prev_n
        self.index = index


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size_of_list = 0

    def add_element(self, data):
        if self.head and self.tail:
            old_tail = self.tail
            self.size_of_list +=1
            new_tail = Node(value = data, next_n = None, prev_n = old_tail, index = old_tail.index+1)
            old_tail.next = new_tail
            self.tail = new_tail
        elif self.head:
            self.tail = Node(value = data, next_n = None, prev_n = self.head, index = 1)
            self.head.next = self.tail
            self.size_of_list +=1
        else:
            self.add_first(data)

    def add_first(self, data):
        if self.head and self.tail:
            old_head = self.head
            self.new_index(old_head, 1)
            self.head = Node(value = data, next_n = old_head, prev_n = None, index = 0)
            old_head.prev = self.head
            self.size_of_list +=1
        elif self.head:
            self.tail = self.head
            self.head = Node(value = data, next_n = self.tail, prev_n = None, index = 0)
            self.tail.prev = self.head
        else:
            self.head = Node(value = data, next_n = self.tail, prev_n = None,index = 0)
            self.tail = None
            self.size_of_list +=1

    def pprint(self):
        node = self.head
        while True:
            if node.next:
                print("{}->".format(node.value),end = '')
            else:
                print("{}".format(node.value), end = '')
            if not node.next:
                break
            node = node.next

    def size(self):
        return self.size_of_list

    def get_index(self, index):
        if self.size_of_list == 0 or index < 0 or index >= self.size_of_list:
            print('No such index!')
        else:
            node = self.head
            while True:
                if node.index == index:
                    return node
                node = node.next

    def remove(self, index):
        if self.size_of_list == 0 or index < 0 or index >= self.size_of_list:
            return

        if index == 0:
            node_to_remove = self.head
            next_node = node_to_remove.next
            self.head = next_node
        else:
            prev_n = self.get_index(index-1)
            node_to_remove = prev_n.next
            next_node = node_to_remove.next
            prev_n.next = next_node

            if index == self.tail.index:
                self.tail = prev_n

        if next_node:
            self.new_index(next_node, -1)

        self.size_of_list -= 1
        return True

    def new_index(self, node, number):
        while True:
            node.index += number
            if not node.next:
                break
            node = node.next

    def remove_last(self, data):
        self.tail = self.tail.prev
        self.tail.next = None

    def to_list(self):
        list_of_linked = []
        if self.head:
            node = self.head
            while True:
                list_of_linked.append(node.value)
                if not node.next:
                    break
                node = node.next
        return list_of_linked

    def add_at_index(self, index, data):
        if(self.size_of_list is 0 and index is 0) or index is 0:
            self.add_first(data)
        elif index < 0 or index > self.size_of_list:
            return print("No such index!!!")
        elif index == self.size_of_list:
            self.add_element(data)
        else:
            prev_n = self.get_index(index-1)
            node_at_index = prev_n.next
            new_node = Node(value = data, next_n = node_at_index, prev_n = prev_n, index = index)
            node_at_index.prev = new_node
            prev_n.next = new_node
            self.new_index(new_node.next, 1)
            self.size_of_list +=1

    def add_last(self, data):
        self.add_element(data)

    def add_list(self, list_to_add: list):
        for el in list_to_add:
            self.add_element(el)

    def add_linked_list(self, linked_list: 'LinkedList'):
        self.add_list(linked_list.to_list())


    def ll_from_to(self, start_index, end_index):
        start_el = self.get_index(start_index)
        new_ll = LinkedList()
        new_ll.add_element(start_el.value)

        while True:
            start_el = start_el.next
            new_ll.add_element(start_el.value)
            if start_el.index == end_index:
                break

        return new_ll

    def pop(self):
        if self.tail:
            self.remove(self.tail.index)
        elif self.head:
            self.head = None
            self.size -=1
        else:
            return False

    def reduce_to_unique(self):
        self_list = self.to_list()
        unique_el = set(self_list)
        unique_list = []
        for el in self_list:
            if el in unique_el:
                unique_el.remove(el)
                unique_list.append(el)
        new_ll = LinkedList()
        new_ll.add_list(unique_list)
        return new_ll

def main():
    # ll = LinkedList()
    # ll.add_element(1)
    # ll.add_element(4)
    # ll.add_element(3)
    # ll.add_element(4)
    # ll.add_element(5)
    # ll.pprint()
    # ll.remove(1)
    # ll.pprint()
    # ll.add_at_index(10, 50)
    # ll.pprint()
    # print(ll.to_list())
    # ll.add_list([5,5,5])
    # ll.pprint()
    # ll.ll_from_to(0, 4).pprint()
    # ll.pprint()
    # # print(ll.size())
    # ll.pop()
    # ll.pop()
    # ll.pop()
    # ll.pprint()
    # print(ll.pop())
    # ll.pprint()
    # unique_ll = ll.reduce_to_unique()
    # unique_ll.pprint()
    pass

if __name__ == "__main__":
    main()
