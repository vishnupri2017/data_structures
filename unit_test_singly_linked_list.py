# test_singly_linked_list.py

import unittest
from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        # Initialize a new singly linked list before each test
        self.sll = SinglyLinkedList()

    def test_empty_list_operations(self):
        # Test deleting from beginning and end on an empty list
        self.sll.delete_from_beginning()
        self.assertEqual(str(self.sll), "None")
        self.sll.delete_from_end()
        self.assertEqual(str(self.sll), "None")
        # Test searching in an empty list
        self.assertEqual(self.sll.search(1), -1)

    def test_single_element_edge_cases(self):
        # Insert single element and test deletions
        self.sll.insert_at_end(10)
        self.assertEqual(str(self.sll), "10 -> None")
        # Delete from beginning
        self.sll.delete_from_beginning()
        self.assertEqual(str(self.sll), "None")

        # Insert again to test delete from end
        self.sll.insert_at_end(20)
        self.assertEqual(str(self.sll), "20 -> None")
        self.sll.delete_from_end()
        self.assertEqual(str(self.sll), "None")

        # Test search on single element list
        self.sll.insert_at_end(30)
        self.assertEqual(self.sll.search(30), 0)
        self.assertEqual(self.sll.search(40), -1)

    def test_multiple_consecutive_operations(self):
        # Perform multiple insertions and deletions
        self.sll.insert_at_beginning(10)
        self.sll.insert_at_beginning(20)
        self.sll.insert_at_end(30)
        self.sll.insert_at_end(40)
        self.assertEqual(str(self.sll), "20 -> 10 -> 30 -> 40 -> None")

        # Perform consecutive deletions
        self.sll.delete_from_beginning()
        self.assertEqual(str(self.sll), "10 -> 30 -> 40 -> None")
        self.sll.delete_from_end()
        self.assertEqual(str(self.sll), "10 -> 30 -> None")

        # Further operations
        self.sll.insert_at_beginning(50)
        self.sll.insert_at_end(60)
        self.assertEqual(str(self.sll), "50 -> 10 -> 30 -> 60 -> None")

        # Final deletion to clear list
        self.sll.delete_from_beginning()
        self.sll.delete_from_beginning()
        self.sll.delete_from_beginning()
        self.sll.delete_from_beginning()
        self.assertEqual(str(self.sll), "None")

    def test_boundary_search(self):
        # Insert elements
        self.sll.insert_at_end(5)
        self.sll.insert_at_end(10)
        self.sll.insert_at_end(15)
        self.sll.insert_at_end(20)

        # Test search for first and last element
        self.assertEqual(self.sll.search(5), 0)
        self.assertEqual(self.sll.search(20), 3)
        self.assertEqual(self.sll.search(25), -1)

    def test_insertions_and_structure(self):
        # Insert elements and test structure
        self.sll.insert_at_beginning(1)
        self.assertEqual(str(self.sll), "1 -> None")
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.assertEqual(str(self.sll), "1 -> 2 -> 3 -> None")
        self.sll.insert_at_beginning(0)
        self.assertEqual(str(self.sll), "0 -> 1 -> 2 -> 3 -> None")


# Run tests
if __name__ == "__main__":
    unittest.main()
