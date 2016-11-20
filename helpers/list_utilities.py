from data_structures.linked_list import LinkedList
from data_structures.node import Node


def to_linked_list(l):
    head = Node(l[0])
    root = LinkedList(head)
    for element in l[1:]:
        root.add(Node(element))
    return root
