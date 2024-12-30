# Singly Linked List Implementation

# Task 1: Node class for Singly Linked List
class Node:
    """
    Node class for a singly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


# Task 2: Singly Linked List with methods for insertion, deletion, and traversal
class SinglyLinkedList:
    """
    Singly Linked List class with insertion, deletion, and traversal methods.
    """
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Task 3: Testing Singly Linked List
print("Singly Linked List Test:")
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.traverse()
sll.delete_node(2)
sll.traverse()
