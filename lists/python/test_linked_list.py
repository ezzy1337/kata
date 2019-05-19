import pytest

from .linked_list import (
    LinkedList,
    DoublyLinkedList
)
from .node import Node
from .exceptions import NodeNotFoundException


########################################
#       Singly Linked List Tests       #
########################################

def test_ll_construct_empty_list():
    subject = LinkedList()
    assert subject == []


def test_ll_add_to_empty_list():
    # arrange
    subject = LinkedList()
    node = Node('a')

    # act
    actual = subject.add(node)

    # assert
    assert actual == 'a'
    assert subject == ['a']


def test_ll_add_to_populated_list():
    # arrange
    subject = LinkedList()

    # setup the nodes to add
    existing_node = Node('existing')
    new_node = Node('new')
    
    # seed the list with a node
    subject.add(existing_node)

    # act
    actual = subject.add(new_node)

    # assert
    assert actual == 'new'
    assert subject == ['existing', 'new']


def test_ll_remove_empty_list():
    subject = LinkedList()

    assert subject.remove('dne') == None
    assert subject == []


def test_ll_remove_first_item_in_list():
    subject = LinkedList()
    subject.add(Node('a'))

    actual = subject.remove('a')
    assert actual == 'a'
    assert subject == []


def test_ll_remove_first_item_in_populated_list():
    subject = LinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))

    actual = subject.remove('first')
    assert actual == 'first'
    assert subject.as_list() == ['second']
    assert subject == ['second']


def test_ll_remove_item_in_middle_of_list():
    subject = LinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('c'))

    assert subject.remove('b') == 'b'
    assert subject == ['a', 'c']


def test_ll_remove_last_item_in_the_list():
    subject = LinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))

    assert subject.remove('b') == 'b'
    assert subject == ['a']


def test_ll_remove_node_that_appears_multiple_times():
    subject = LinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('b'))
    subject.add(Node('c'))

    assert subject.remove('b') == 'b'
    assert subject == ['a', 'b', 'c']


########################################
#       Doubly Linked List Tests       #
########################################

def test_dl_construct_empty_list():
    subject = DoublyLinkedList()
    assert subject == []


def test_dl_add_to_empty_list():
    subject = DoublyLinkedList()

    node = Node('a')
    subject.add(node)

    assert subject == ['a']


def test_dl_add_to_populated_list():
    subject = DoublyLinkedList()
    subject.add(Node('existing'))

    node = Node('new')
    subject.add(node)

    assert subject == ['existing', 'new']


def test_dl_remove_empty_list():
    subject = DoublyLinkedList()
    subject.remove('dne')

    assert subject == []


def test_dl_remove_first_item():
    subject = DoublyLinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))

    subject.remove('first')

    assert subject == ['second']


def test_dl_remove_last_item():
    subject = DoublyLinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))

    subject.remove('second')

    assert subject.as_list() == ['first']
    assert subject == ['first']


def test_dl_remove_item_in_middle_of_list():
    subject = DoublyLinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))
    subject.add(Node('third'))

    subject.remove('second')

    assert subject == ['first', 'third']


def test_dl_remove_node_that_appears_multiple_times():
    subject = DoublyLinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('c'))
    subject.add(Node('b'))

    subject.remove('b')

    assert subject == ['a', 'c', 'b']
