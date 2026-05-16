from linkedlist import LinkedList, Node


class IsEmptyError(Exception):
    """Error raised when trying to pop/dequeue items from an empty
    Stack/Queue.
    """
    pass


class Stack(LinkedList):
    """Implements the Stack ADT using a linkedlist.

    Arguments
        None

    Methods
        - push(item) -> None
        - pop() -> item
    """

    def __repr__(self) -> str:
        return 'Stack()'

    def push(self, item: tuple[int, int]) -> None:
        """Pushes item onto the top of the stack.
        
        Arguments
            - item
              The item to be pushed.
        
        Returns
            None
        """
        self.insert(0, item)

        
    def pop(self) -> tuple[int, int]:
        """Pops item off the top of the stack, and returns it.

        Arguments
            None

        Returns
            item

        Raises
            Empty - if stack is already empty
        """
        if self.length() == 0:
            raise IsEmptyError('the stack is already empty')

        value = self.get(0)
        self.delete(0)
        return value

        


# Queue can also inherit from Array
class Queue(LinkedList):
    """Implements the Queue ADT using a linkedlist.

    Arguments
        None

    Methods
        - enqueue(item) -> None
        - dequeue() -> item
    """

    def __repr__(self) -> str:
        return 'Queue()'

    def enqueue(self, item: tuple[int, int]) -> None:
        """Enqueues item into the end of the queue.

        Arguments
            - item
              The item to be enqueued.

        Returns
            None
        """
        self.append(item)

    def dequeue(self) -> tuple[int, int]:
        """Dequeues item from the front of the queue, and returns it.

        Arguments
            None

        Returns
            item

        Raises
            Empty - if queue is already empty
        """
        if self.length == 0:
            raise IsEmptyError('queue is empty')

        value = self.get(0)
        self.delete(0)
        return value


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python adt.py`
    pass
