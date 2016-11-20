from data_structures.linked_list import LinkedList
from data_structures.node import Node


def test_add():
    first = Node('first')
    second = Node('second')
    l = LinkedList(first)
    l.add(second)

    assert l.node.value == 'first'
    assert l.node.next.value == 'second'


def test_remove():
    first = Node('first')
    second = Node('second')
    l = LinkedList(first)
    l.add(second)

    l.remove('second')
    assert not l.node.next
    assert l.node.value == 'first'
