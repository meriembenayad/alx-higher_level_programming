#!/usr/bin/python3
""" Define a class Node """


class Node:
    """
    Represents a node object.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node object.

        Args:
            data (int): Data value of the node.
            next_node (Node): Reference to the next node. Defaults to None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter property for the data value of the node.

        Returns:
            int: Data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter property for the data value of the node.

        Args:
            value (int): New data value for the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter property for the reference to the next node.

        Returns:
            Node: Reference to the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter property for the reference to the next node.

        Args:
            value (Node): New reference to the next node.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts a new Node
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                    current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        nodes = []
        current_node = self.__head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next_node
        return '\n'.join(nodes)
