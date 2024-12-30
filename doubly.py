# Doubly Linked List Implementation

# Task 1: Node class for Doubly Linked List
class DoublyNode:
    """
    Node class for a doubly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Task 2: Doubly Linked List with methods for insertion, deletion, and traversal
class DoublyLinkedList:
    """
    Doubly Linked List class with insertion, deletion, and traversal methods.
    """
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_node(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                temp = None
                return
            temp = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Task 3: Testing Doubly Linked List
print("\nDoubly Linked List Test:")
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.traverse()
dll.delete_node(2)
dll.traverse()
