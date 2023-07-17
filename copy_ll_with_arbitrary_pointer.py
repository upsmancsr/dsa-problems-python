# Copy linked list with arbitrary pointer
# You are given a linked list where the node has two pointers.
# The first is the regular next pointer. 
# The second pointer is called arbitrary_pointer and it can point to any node in the linked list. 
# Your job is to write code to make a deep copy of the given linked list. 
# Here, deep copy means that any operations on the original list 
# (inserting, modifying and removing) should not affect the copied list.

# Create a Node class to contain a value, next, and arbitraty_pointer
class Node:
    def __init__(self, x, next=None, arbitrary_pointer=None):
        self.value = x
        self.next = next
        self.arbitraty_pointer = arbitrary_pointer

    def deep_copy(head):
        