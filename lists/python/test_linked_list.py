import pytest

from .linked_list import (
    LinkedList,
    DoublyLinkedList,
    CircularList,
    is_valid
)
from .node import Node
from .exceptions import NodeNotFoundException

########################################
#       Singly Linked List Tests       #
########################################

def test_sl_construct_empty_list():
    subject = LinkedList()
    assert subject == []


def test_sl_add_to_empty_list():
    # arrange
    subject = LinkedList()
    node = Node('a')

    # act
    actual = subject.add(node)

    # assert
    assert actual == node
    assert subject == ['a']


def test_sl_add_to_populated_list():
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
    assert actual == new_node
    assert subject == ['existing', 'new']


def test_sl_remove_empty_list():
    # arrange
    subject = LinkedList()
    
    # act/assert
    assert subject.remove('dne') == None
    assert subject == []


def test_sl_remove_first_item_in_list():
    # arrange
    subject = LinkedList()
    node = Node('a')
    subject.add(node)

    # act
    actual = subject.remove(node)

    # assert
    assert actual == node
    assert subject == []


def test_sl_remove_first_item_in_populated_list():
    # arrange
    subject = LinkedList()
    remove_node = Node('first')
    subject.add(remove_node)
    subject.add(Node('second'))

    #act
    actual = subject.remove(remove_node)
    
    # assert
    assert actual == remove_node
    assert subject.as_list() == ['second']
    assert subject == ['second']


def test_sl_remove_item_in_middle_of_list():
    # arrange
    subject = LinkedList()
    subject.add(Node('a'))
    remove_node = Node('b')
    subject.add(remove_node)
    subject.add(Node('c'))

    # act/assert
    assert subject.remove(remove_node) == remove_node
    assert subject == ['a', 'c']


def test_sl_remove_last_item_in_the_list():
    # arrange
    subject = LinkedList()
    subject.add(Node('a'))
    remove_node = Node('b')
    subject.add(remove_node)

    # act/assert
    assert subject.remove(remove_node) == remove_node
    assert subject == ['a']


def test_sl_remove_node_that_appears_multiple_times():
    # arrange
    subject = LinkedList()
    subject.add(Node('a'))
    dup_value_node1 = Node('b')
    dup_value_node2 = Node('b')
    subject.add(dup_value_node1)
    subject.add(dup_value_node2)
    subject.add(Node('c'))

    # act/assert
    assert subject.remove(dup_value_node1) == dup_value_node1
    assert subject == ['a', 'b', 'c']


########################################
#       Doubly Linked List Tests       #
########################################

def test_dl_construct_empty_list():
    # arrange
    subject = DoublyLinkedList()

    # act/assert
    assert subject == []


def test_dl_add_to_empty_list():
    # arrange
    subject = DoublyLinkedList()

    #act
    node = Node('a')
    subject.add(node)

    # assert
    assert subject == ['a']


def test_dl_add_to_populated_list():
    subject = DoublyLinkedList()
    subject.add(Node('existing'))

    #act
    node = Node('new')
    subject.add(node)

    # assert
    assert subject == ['existing', 'new']


def test_dl_remove_empty_list():
    # arrange
    subject = DoublyLinkedList()
    #act
    subject.remove('dne')

    # assert
    assert subject == []


def test_dl_remove_first_item():
    # arrange
    subject = DoublyLinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))

    #act
    subject.remove('first')

    # assert
    assert subject == ['second']


def test_dl_remove_last_item():
    # arrange
    subject = DoublyLinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))

    #act
    subject.remove('second')

    # assert
    assert subject.as_list() == ['first']
    assert subject == ['first']

#16
def test_dl_remove_item_in_middle_of_list():
    # arrange
    subject = DoublyLinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))
    subject.add(Node('third'))

    #act
    subject.remove('second')

    # assert
    assert subject == ['first', 'third']


def test_dl_remove_node_that_appears_multiple_times():
    # arrange
    subject = DoublyLinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('c'))
    subject.add(Node('b'))

    #act
    subject.remove('b')

    # assert
    assert subject == ['a', 'c', 'b']

########################################
#     Circularly Linked List Tests     #
########################################


def test_cl_construct_empty_list():
    # arrange
    subject = CircularList()
    
    # act/assert
    assert subject == []


def test_cl_add_to_empty_list():
    # arrange
    subject = CircularList()
    nodeA = Node('a')

    #act
    actual = subject.add(nodeA)

    # assert
    assert actual == node
    assert subject == ['a']


def test_cl_add_to_populated_list():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))
    nodeB = Node('b')

    #act
    actual = subject.add(nodeB)

    # assert
    assert actual == nodeB
    assert subject == ['a', 'b']

#21
def test_cl_add_to_list_of_2_plus():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    nodeC = Node('c')
    
    #act
    actual = subject.add(nodeC)

    # assert
    assert actual == nodeC
    assert subject.as_list() == ['a', 'b', 'c']
    assert subject == ['a', 'b', 'c']


def test_cl_remove_empty_list():
    # arrange
    subject = CircularList()
    node = Node('dne')

    # assert
    assert subject.remove(node) is None


def test_cl_remove_only_item():
    # arrange
    subject = CircularList()
    nodeA = Node('a')
    subject.add(nodeA)

    #act
    actual = subject.remove(NodeA)

    # assert
    assert actual == NodeA
    assert subject == []


def test_cl_remove_first_item_in_list():
    # arrange
    subject = CircularList()
    nodeA = Node('a')
    subject.add(NodeA)
    subject.add(Node('b'))

    #act
    actual = subject.remove(nodeA)

    # assert
    assert actual== nodeA
    assert subject == ['b']


def test_cl_remove_last_item_in_list():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))
    nodeB = Node('b')
    subject.add(nodeB)

    #act
    actual = subject.remove(NodeB)

    # assert
    assert actual == nodeB
    assert subject == ['a']

def test_cl_remove_item_from_middle_of_list():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('c'))
    nodeD = Node('d')
    subject.add(nodeD)
    subject.add(Node('e'))
    subject.add(Node('f'))

    #act
    actual = subject.remove(nodeD)

    # assert
    assert actual == nodeD
    assert subject == ['a', 'b', 'c', 'e', 'f']

########################################
#     Using Linked List as a Stack     #
########################################

def test_alg_is_valid():
    test = '()'
    assert is_valid(test) is True


def test_alg_is_not_valid():
    test = '('
    assert is_valid(test) is False


def test_alg_out_of_order():
    assert is_valid('({)}') == False
