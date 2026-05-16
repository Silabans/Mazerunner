"""datastruct.py

# Data Structures

This module defines the LinkedList abstract data type
"""
############################### 72 chars ###############################


class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """
    def __init__(self, data: tuple[int, int]):
        self.next = None
        self.data = data


    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """
        return self.data


class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        current = self._head
        length = 0
        while current:
            length += 1
            current = current.next
        return length
        

    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Returns
            item

        Raises
            IndexError if n >= length
        """
        length = self.length()
        if n >= length:
            raise IndexError
        current = self._head
        for i in range(n):
            current = current.next
        return current.get()


    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """

        length = self.length()
        if n > length:
            raise IndexError('The position n exceeds the length of the LinkedList.')
        new_node = Node(item)

        if n == 0:
            new_node.next = self._head
            self._head = new_node
            return

        current_length = 0
        current = self._head



        while current_length < (n - 1):
            current_length += 1
            current = current.next
        
        n_node = current.next
        current.next = new_node
        new_node.next = n_node
        return

    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        length = self.length()
        if length == 0:
            self._head = Node(item)
            return
        current = self._head
        for i in range(length - 1):
            current = current.next
        new_node = Node(item)
        current.next = new_node
        return



    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Raises
            IndexError if n >= length
        """
        length = self.length()
        if n == 0:
            to_be_deleted = self._head
            self._head = to_be_deleted.next
            return
        elif n >= length:
                raise IndexError
        current = self._head
        for i in range(n - 1):
            current = current.next
        previous = current
        to_be_deleted = current.next
        next_node = to_be_deleted.next
        previous.next = next_node
        return
        
       
    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        length = self.length()
        current = self._head
        for i in range(length):
            if current.get() == item:
                return True
            current = current.next
        return False



if __name__ == "__main__":
    # Write any test code here and run it with
    # `python datastruct.py`
    list_1 = LinkedList()
    node_1 = Node((1,1))
    node_2 = Node((1,2))
    node_3 = Node((1,3))
    node_4 = Node((2,1))
    node_5 = Node((2,2))
    node_6 = Node((2,3))
    nodes = [node_1, node_2, node_3, node_4, node_5, node_6]
    for node in nodes:
        list_1.append(node)
    list_1.delete(0)
    print(list_1.length())
    
