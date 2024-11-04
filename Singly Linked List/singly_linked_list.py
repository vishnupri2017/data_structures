import unittest

class Node:
    def __init__(self, data):
        self.data = data # the data that is held by the node
        self.next = None # pointer to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head # we are inserting in the beginning so
                                # the current head has to be the next element

        self.head = new_node # head points to new node

    def insert_at_end(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(position - 1):
            if current is None:
                raise IndexError("Out of bounds index")
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_from_end(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None

        current_node = self.head

        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def delete_at_position(self,position):
        if position == 0:
            self.head = self.head.next
            return

        current = self.head

        for i in range(position-1):
            if current.next is None:
                raise IndexError("position not found")
            current = current.next

        current.next = current.next.next

    def search(self, key):
        current = self.head
        position = 0

        while current:
            if current.data == key:
                return position

            current = current.next
            position += 1

        return -1

    def __str__(self):
        nodes = []
        curr = self.head

        while curr:
            nodes.append(str(curr.data))
            curr = curr.next

        return "->".join(nodes) + "-> None"
    # def traverse(self):
    #     current = self.head
    #     while current:
    #         print(current.data, end="->")
    #         current = current.next
    #
    #     print("None")

sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_beginning(20)
sll.insert_at_end(40)
sll.insert_at_end(59)




